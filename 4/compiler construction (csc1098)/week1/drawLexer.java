// Generated from draw.g4 by ANTLR 4.13.2
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue", "this-escape"})
public class drawLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.13.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		Up=1, Down=2, Left=3, Right=4, Init=5, Draw=6, Display=7, NUMBER=8, WS=9;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"A", "D", "E", "F", "G", "H", "I", "L", "N", "O", "P", "R", "S", "T", 
			"U", "W", "Y", "Up", "Down", "Left", "Right", "Init", "Draw", "Display", 
			"NUMBER", "WS"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "Up", "Down", "Left", "Right", "Init", "Draw", "Display", "NUMBER", 
			"WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}


	public drawLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "draw.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\u0004\u0000\t\u0088\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002\u0001"+
		"\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004"+
		"\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007"+
		"\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b"+
		"\u0007\u000b\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002"+
		"\u000f\u0007\u000f\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002"+
		"\u0012\u0007\u0012\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014\u0002"+
		"\u0015\u0007\u0015\u0002\u0016\u0007\u0016\u0002\u0017\u0007\u0017\u0002"+
		"\u0018\u0007\u0018\u0002\u0019\u0007\u0019\u0001\u0000\u0001\u0000\u0001"+
		"\u0001\u0001\u0001\u0001\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001"+
		"\u0004\u0001\u0004\u0001\u0005\u0001\u0005\u0001\u0006\u0001\u0006\u0001"+
		"\u0007\u0001\u0007\u0001\b\u0001\b\u0001\t\u0001\t\u0001\n\u0001\n\u0001"+
		"\u000b\u0001\u000b\u0001\f\u0001\f\u0001\r\u0001\r\u0001\u000e\u0001\u000e"+
		"\u0001\u000f\u0001\u000f\u0001\u0010\u0001\u0010\u0001\u0011\u0001\u0011"+
		"\u0001\u0011\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012"+
		"\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0014"+
		"\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0015"+
		"\u0001\u0015\u0001\u0015\u0001\u0015\u0001\u0015\u0001\u0016\u0001\u0016"+
		"\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0017\u0001\u0017\u0001\u0017"+
		"\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0018"+
		"\u0004\u0018~\b\u0018\u000b\u0018\f\u0018\u007f\u0001\u0019\u0004\u0019"+
		"\u0083\b\u0019\u000b\u0019\f\u0019\u0084\u0001\u0019\u0001\u0019\u0000"+
		"\u0000\u001a\u0001\u0000\u0003\u0000\u0005\u0000\u0007\u0000\t\u0000\u000b"+
		"\u0000\r\u0000\u000f\u0000\u0011\u0000\u0013\u0000\u0015\u0000\u0017\u0000"+
		"\u0019\u0000\u001b\u0000\u001d\u0000\u001f\u0000!\u0000#\u0001%\u0002"+
		"\'\u0003)\u0004+\u0005-\u0006/\u00071\b3\t\u0001\u0000\u0013\u0002\u0000"+
		"AAaa\u0002\u0000DDdd\u0002\u0000EEee\u0002\u0000FFff\u0002\u0000GGgg\u0002"+
		"\u0000HHhh\u0002\u0000IIii\u0002\u0000LLll\u0002\u0000NNnn\u0002\u0000"+
		"OOoo\u0002\u0000PPpp\u0002\u0000RRrr\u0002\u0000SSss\u0002\u0000TTtt\u0002"+
		"\u0000UUuu\u0002\u0000WWww\u0002\u0000YYyy\u0001\u000009\u0003\u0000\t"+
		"\n\r\r  x\u0000#\u0001\u0000\u0000\u0000\u0000%\u0001\u0000\u0000\u0000"+
		"\u0000\'\u0001\u0000\u0000\u0000\u0000)\u0001\u0000\u0000\u0000\u0000"+
		"+\u0001\u0000\u0000\u0000\u0000-\u0001\u0000\u0000\u0000\u0000/\u0001"+
		"\u0000\u0000\u0000\u00001\u0001\u0000\u0000\u0000\u00003\u0001\u0000\u0000"+
		"\u0000\u00015\u0001\u0000\u0000\u0000\u00037\u0001\u0000\u0000\u0000\u0005"+
		"9\u0001\u0000\u0000\u0000\u0007;\u0001\u0000\u0000\u0000\t=\u0001\u0000"+
		"\u0000\u0000\u000b?\u0001\u0000\u0000\u0000\rA\u0001\u0000\u0000\u0000"+
		"\u000fC\u0001\u0000\u0000\u0000\u0011E\u0001\u0000\u0000\u0000\u0013G"+
		"\u0001\u0000\u0000\u0000\u0015I\u0001\u0000\u0000\u0000\u0017K\u0001\u0000"+
		"\u0000\u0000\u0019M\u0001\u0000\u0000\u0000\u001bO\u0001\u0000\u0000\u0000"+
		"\u001dQ\u0001\u0000\u0000\u0000\u001fS\u0001\u0000\u0000\u0000!U\u0001"+
		"\u0000\u0000\u0000#W\u0001\u0000\u0000\u0000%Z\u0001\u0000\u0000\u0000"+
		"\'_\u0001\u0000\u0000\u0000)d\u0001\u0000\u0000\u0000+j\u0001\u0000\u0000"+
		"\u0000-o\u0001\u0000\u0000\u0000/t\u0001\u0000\u0000\u00001}\u0001\u0000"+
		"\u0000\u00003\u0082\u0001\u0000\u0000\u000056\u0007\u0000\u0000\u0000"+
		"6\u0002\u0001\u0000\u0000\u000078\u0007\u0001\u0000\u00008\u0004\u0001"+
		"\u0000\u0000\u00009:\u0007\u0002\u0000\u0000:\u0006\u0001\u0000\u0000"+
		"\u0000;<\u0007\u0003\u0000\u0000<\b\u0001\u0000\u0000\u0000=>\u0007\u0004"+
		"\u0000\u0000>\n\u0001\u0000\u0000\u0000?@\u0007\u0005\u0000\u0000@\f\u0001"+
		"\u0000\u0000\u0000AB\u0007\u0006\u0000\u0000B\u000e\u0001\u0000\u0000"+
		"\u0000CD\u0007\u0007\u0000\u0000D\u0010\u0001\u0000\u0000\u0000EF\u0007"+
		"\b\u0000\u0000F\u0012\u0001\u0000\u0000\u0000GH\u0007\t\u0000\u0000H\u0014"+
		"\u0001\u0000\u0000\u0000IJ\u0007\n\u0000\u0000J\u0016\u0001\u0000\u0000"+
		"\u0000KL\u0007\u000b\u0000\u0000L\u0018\u0001\u0000\u0000\u0000MN\u0007"+
		"\f\u0000\u0000N\u001a\u0001\u0000\u0000\u0000OP\u0007\r\u0000\u0000P\u001c"+
		"\u0001\u0000\u0000\u0000QR\u0007\u000e\u0000\u0000R\u001e\u0001\u0000"+
		"\u0000\u0000ST\u0007\u000f\u0000\u0000T \u0001\u0000\u0000\u0000UV\u0007"+
		"\u0010\u0000\u0000V\"\u0001\u0000\u0000\u0000WX\u0003\u001d\u000e\u0000"+
		"XY\u0003\u0015\n\u0000Y$\u0001\u0000\u0000\u0000Z[\u0003\u0003\u0001\u0000"+
		"[\\\u0003\u0013\t\u0000\\]\u0003\u001f\u000f\u0000]^\u0003\u0011\b\u0000"+
		"^&\u0001\u0000\u0000\u0000_`\u0003\u000f\u0007\u0000`a\u0003\u0005\u0002"+
		"\u0000ab\u0003\u0007\u0003\u0000bc\u0003\u001b\r\u0000c(\u0001\u0000\u0000"+
		"\u0000de\u0003\u0017\u000b\u0000ef\u0003\r\u0006\u0000fg\u0003\t\u0004"+
		"\u0000gh\u0003\u000b\u0005\u0000hi\u0003\u001b\r\u0000i*\u0001\u0000\u0000"+
		"\u0000jk\u0003\r\u0006\u0000kl\u0003\u0011\b\u0000lm\u0003\r\u0006\u0000"+
		"mn\u0003\u001b\r\u0000n,\u0001\u0000\u0000\u0000op\u0003\u0003\u0001\u0000"+
		"pq\u0003\u0017\u000b\u0000qr\u0003\u0001\u0000\u0000rs\u0003\u001f\u000f"+
		"\u0000s.\u0001\u0000\u0000\u0000tu\u0003\u0003\u0001\u0000uv\u0003\r\u0006"+
		"\u0000vw\u0003\u0019\f\u0000wx\u0003\u0015\n\u0000xy\u0003\u000f\u0007"+
		"\u0000yz\u0003\u0001\u0000\u0000z{\u0003!\u0010\u0000{0\u0001\u0000\u0000"+
		"\u0000|~\u0007\u0011\u0000\u0000}|\u0001\u0000\u0000\u0000~\u007f\u0001"+
		"\u0000\u0000\u0000\u007f}\u0001\u0000\u0000\u0000\u007f\u0080\u0001\u0000"+
		"\u0000\u0000\u00802\u0001\u0000\u0000\u0000\u0081\u0083\u0007\u0012\u0000"+
		"\u0000\u0082\u0081\u0001\u0000\u0000\u0000\u0083\u0084\u0001\u0000\u0000"+
		"\u0000\u0084\u0082\u0001\u0000\u0000\u0000\u0084\u0085\u0001\u0000\u0000"+
		"\u0000\u0085\u0086\u0001\u0000\u0000\u0000\u0086\u0087\u0006\u0019\u0000"+
		"\u0000\u00874\u0001\u0000\u0000\u0000\u0003\u0000\u007f\u0084\u0001\u0006"+
		"\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}