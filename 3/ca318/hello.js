const token = "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"

const url = "https://api.openai.com/v1/chat/completions"

fetch(url, {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
        'Authorizaation': 'Bearer ' + token,
    },
    data: JSON.stringify({
        'model': 'gpt-3.5-turbo',
        'messages': [{"role": "user", "content": "Say 'Hello, world!'"}]
    })
})
.then(response => {
    const result = response.json();
    console.log(result)
})