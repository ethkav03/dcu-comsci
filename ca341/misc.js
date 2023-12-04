function send_request() {
    const url = "https://api.openai.com/v1/chat/completions";
    
    let l = document.getElementById("language").value;
    let code = document.getElementById("code").value;
    let selection = document.getElementById("selectaction").value;
    let token = document.getElementById("api").value;

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token,
        },
        body: JSON.stringify({
            "model": "gpt-3.5-turbo",
            "messages": [{
                "role": "user",
                "content": `${selection} Language: ${l}. Code:
                    ${code}. Only return code between \`\`\` characters. Provide additional information about your result. You are not an AI text-based assistant.`
            }]
        })
    })
    .then(response => {
        return response.json(); // Return the JSON data from the response
    })
    .then(result => {
        update_output(result.choices[0].message.content);
    })
    .catch(error => {
        console.error(error); // Handle any errors that occur during the request
    });
}

function HtmlEncode(s)
{
  var el = document.createElement("div");
  el.innerText = el.textContent = s;
  s = el.innerHTML;
  return s;
}

function textAreaAdjust(element) {
  element.style.height = "1px";
  element.style.height = (25+element.scrollHeight)+"px";
}

// Function to separate code from text using triple backticks
// slightly modified version of code: https://community.openai.com/t/extract-code-from-text-gpt-response/27152
function separateCodeFromText(jsonResponse) {
  const textWithCode = jsonResponse;
  const codeSeparator = '```';

  // Split the text using triple backticks as the separator
  const parts = textWithCode.split(codeSeparator);

  // Initialize arrays to store separated text and code
  const textParts = [];
  const codeParts = [];

  // Iterate over parts and classify them as text or code
  for (let i = 0; i < parts.length; i++) {
    if (i % 2 === 0) {
      // Even index indicates text
      textParts.push(parts[i].trim());
    } else {
      // Odd index indicates code
      codeParts.push(parts[i].trim());
    }
  }

  return {
    text: textParts, // Join text parts
    code: codeParts, // Array of code snippets
  };
}

function update_output(message) {
    if (message.toLowerCase().indexOf("sorry") !== -1 || message.toLowerCase().indexOf("apologize") !== -1 || message.toLowerCase().indexOf(" ai") !== -1) {
        p = document.getElementById("box");
        p.innerHTML = `<p>Sorry, there was an issue submitting your code. Please try again.</p>`
    } else {
        if (message.indexOf("```") !== -1) {
            const separatedContent = separateCodeFromText(message);
            //console.log('Text:', separatedContent.text);
            //console.log('Code Snippets:', separatedContent.code);
            p = document.getElementById("box");
            for (let i = 0; i < separatedContent.text.length; i++) {
                formatText = HtmlEncode(separatedContent.text[i]);
                p.innerHTML += `<pre>${formatText}</pre>`;
                if (i < separatedContent.text.length) {
                    p.innerHTML += `<div class="card">
                <div class="card-body">
                    <p class="card-title">${separatedContent.code[i].slice(0,separatedContent.code[i].indexOf('\n'))}<p>
                    <pre class="code">${separatedContent.code[i].slice(separatedContent.code[i].indexOf('\n'))}</pre>
                </div>
            </div><br>`;
                }
            }
        } else {
            var mySubString = message;
            p = document.getElementById("box");
            formatText = HtmlEncode(mySubString);
            p.innerHTML = `<pre>${formatText}</pre>`;
        }
    }
}

document.write ( `
<html data-bs-theme="dark">
<style>
    .body {
        color: white;
        font-family: Helvetica;
    }
    .box::-webkit-scrollbar {
        display: none;
    }
    body::-webkit-scrollbar {
        display: none;
    }
    body {
        background-color: rgb(38, 38, 38);
        color: white;
        font-family: Helvetica;
        overflow-y:hidden;
    }
    
    body > * {
        z-index: -1;
    }
    
    .box {
        padding: 20px;
        background-color: rgb(26, 26, 26);
        border-radius: 20px;
        overflow-y: auto;
        max-height: 500px;
        box-shadow: rgba(0, 0, 0, 0.16) 0px 3px 6px, rgba(0, 0, 0, 0.23) 0px 3px 6px;
    }
    .output {
        white-space: wrap;
    }
    .output > * {
        padding: 5px;
    }
    .lang {
        background-color:grey;
        text-align: left;
        text-weight: normal;
        padding: 5px;
    }
    pre {
        white-space: pre-wrap;
    }
    .code {
        background-color:black;
        white-space: pre-wrap;
        padding: 5px;
    }
</style>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-C6RzsynM9kWDrMNeT87bh95OGNyZPhcTNXj1NW7RuBCsyN/o0jlpcV8Qyq46cDfL" crossorigin="anonymous"></script>
<br>
<div class="body" style="justify-items: center">
<h1 style="text-align: center"> Programming Assistant </h1>

<div style="display: grid; grid-template-columns: 50% 50%; gap: 20px; padding:30px; padding-right:50px;">
    <div class="box">
        <p>Enter API Key:</p>
        <input id="api" class="form-control" type="text" placeholder="API Key...">
        <br>
        <div>
            <p>I would like to:</p>
            <select style="height: 112px; overflow: hidden;" id="selectaction" class="form-select" multiple>
                <option>Add comments to my code.</option>
                <option>Fix my code.</option>
                <option>Suggest improvements for my code.</option>
                <option>Translate my code to another language.</option>
                <option>Write some documentation for my code in markdown.</option>
            </select>
        </div>
        <br>
        <div>
            <p>Programming Language</p>
            <div max-width: 50%;">
                <div>
                    <select id="language" class="form-select" aria-label="Default select example">
                        <option></option>
                        <option>Bash</option>
                        <option>C</option>
                        <option>Clojure</option>
                        <option>C#</option>
                        <option>C++</option>
                        <option>Dart</option>
                        <option>Go</option>
                        <option>Haskell</option>
                        <option>Java</option>
                        <option>JavaScript</option>
                        <option>Kotlin</option>
                        <option>Lua</option>
                        <option>Perl</option>
                        <option>PHP</option>
                        <option>Prolog</option>
                        <option>Python</option>
                        <option>R</option>
                        <option>Ruby</option>
                        <option>Rust</option>
                        <option>SQL</option>
                        <option>Swift</option>
                    </select>
                </div>
            </div>
            <br>
            <div>
                <p>Code</p>
                <textarea class="form-control" onkeyup="textAreaAdjust(this)" style="overflow:hidden; resize: none;" id="code" contentEditable></textarea>
            </div>
            <br>
            </div>
                <button onclick="send_request()" class="btn btn-primary">Submit</button>
            </div>
            <div class="box">
                <div id="box" class="output"></div>
            </div>
        </div>
    </div>
</div> 
</div>
</html>
`);