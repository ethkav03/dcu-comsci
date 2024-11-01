import org.antlr.v4.runtime.CharStreams;
import org.antlr.v4.runtime.CommonTokenStream;
import org.antlr.v4.runtime.tree.ParseTree;

import java.io.IOException;

public class CALParserMain {

    public static void main(String[] args) {
        if (args.length != 1) {
            System.err.println("Usage: java CALParserMain <filename>");
            System.exit(1);
        }

        String filename = args[0];
        try {
            // Create a lexer and parser for the input file
            CALLexer lexer = new CALLexer(CharStreams.fromFileName(filename));
            CommonTokenStream tokens = new CommonTokenStream(lexer);
            CALParser parser = new CALParser(tokens);

            // Parse the input file starting from the 'program' rule
            ParseTree tree = parser.program();

            // Check for parsing errors
            if (parser.getNumberOfSyntaxErrors() == 0) {
                System.out.println(filename + " parsed successfully");
            } else {
                System.out.println(filename + " has not parsed");
            }

        } catch (IOException e) {
            System.err.println("Error reading file: " + filename);
            e.printStackTrace();
        }
    }
}
