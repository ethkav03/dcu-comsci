// Generated from draw.g4 by ANTLR 4.13.2
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue", "this-escape"})
public class drawParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		Up=1, Down=2, Left=3, Right=4, Init=5, Draw=6, Display=7, NUMBER=8, WS=9;
	public static final int
		RULE_prog = 0, RULE_stm = 1;
	private static String[] makeRuleNames() {
		return new String[] {
			"prog", "stm"
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

	@Override
	public String getGrammarFileName() { return "draw.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public drawParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgContext extends ParserRuleContext {
		public List<StmContext> stm() {
			return getRuleContexts(StmContext.class);
		}
		public StmContext stm(int i) {
			return getRuleContext(StmContext.class,i);
		}
		public ProgContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_prog; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof drawVisitor ) return ((drawVisitor<? extends T>)visitor).visitProg(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ProgContext prog() throws RecognitionException {
		ProgContext _localctx = new ProgContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_prog);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(7);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 254L) != 0)) {
				{
				{
				setState(4);
				stm();
				}
				}
				setState(9);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StmContext extends ParserRuleContext {
		public StmContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_stm; }
	 
		public StmContext() { }
		public void copyFrom(StmContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class InitContext extends StmContext {
		public TerminalNode Init() { return getToken(drawParser.Init, 0); }
		public List<TerminalNode> NUMBER() { return getTokens(drawParser.NUMBER); }
		public TerminalNode NUMBER(int i) {
			return getToken(drawParser.NUMBER, i);
		}
		public InitContext(StmContext ctx) { copyFrom(ctx); }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof drawVisitor ) return ((drawVisitor<? extends T>)visitor).visitInit(this);
			else return visitor.visitChildren(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class LeftContext extends StmContext {
		public TerminalNode Left() { return getToken(drawParser.Left, 0); }
		public LeftContext(StmContext ctx) { copyFrom(ctx); }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof drawVisitor ) return ((drawVisitor<? extends T>)visitor).visitLeft(this);
			else return visitor.visitChildren(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class DisplayContext extends StmContext {
		public TerminalNode Display() { return getToken(drawParser.Display, 0); }
		public DisplayContext(StmContext ctx) { copyFrom(ctx); }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof drawVisitor ) return ((drawVisitor<? extends T>)visitor).visitDisplay(this);
			else return visitor.visitChildren(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class UpContext extends StmContext {
		public TerminalNode Up() { return getToken(drawParser.Up, 0); }
		public UpContext(StmContext ctx) { copyFrom(ctx); }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof drawVisitor ) return ((drawVisitor<? extends T>)visitor).visitUp(this);
			else return visitor.visitChildren(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class RightContext extends StmContext {
		public TerminalNode Right() { return getToken(drawParser.Right, 0); }
		public RightContext(StmContext ctx) { copyFrom(ctx); }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof drawVisitor ) return ((drawVisitor<? extends T>)visitor).visitRight(this);
			else return visitor.visitChildren(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class DrawContext extends StmContext {
		public TerminalNode Draw() { return getToken(drawParser.Draw, 0); }
		public DrawContext(StmContext ctx) { copyFrom(ctx); }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof drawVisitor ) return ((drawVisitor<? extends T>)visitor).visitDraw(this);
			else return visitor.visitChildren(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class DownContext extends StmContext {
		public TerminalNode Down() { return getToken(drawParser.Down, 0); }
		public DownContext(StmContext ctx) { copyFrom(ctx); }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof drawVisitor ) return ((drawVisitor<? extends T>)visitor).visitDown(this);
			else return visitor.visitChildren(this);
		}
	}

	public final StmContext stm() throws RecognitionException {
		StmContext _localctx = new StmContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_stm);
		try {
			setState(19);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case Init:
				_localctx = new InitContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(10);
				match(Init);
				setState(11);
				match(NUMBER);
				setState(12);
				match(NUMBER);
				}
				break;
			case Up:
				_localctx = new UpContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(13);
				match(Up);
				}
				break;
			case Down:
				_localctx = new DownContext(_localctx);
				enterOuterAlt(_localctx, 3);
				{
				setState(14);
				match(Down);
				}
				break;
			case Right:
				_localctx = new RightContext(_localctx);
				enterOuterAlt(_localctx, 4);
				{
				setState(15);
				match(Right);
				}
				break;
			case Left:
				_localctx = new LeftContext(_localctx);
				enterOuterAlt(_localctx, 5);
				{
				setState(16);
				match(Left);
				}
				break;
			case Draw:
				_localctx = new DrawContext(_localctx);
				enterOuterAlt(_localctx, 6);
				{
				setState(17);
				match(Draw);
				}
				break;
			case Display:
				_localctx = new DisplayContext(_localctx);
				enterOuterAlt(_localctx, 7);
				{
				setState(18);
				match(Display);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\u0004\u0001\t\u0016\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0001"+
		"\u0000\u0005\u0000\u0006\b\u0000\n\u0000\f\u0000\t\t\u0000\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0003\u0001\u0014\b\u0001\u0001\u0001\u0000\u0000"+
		"\u0002\u0000\u0002\u0000\u0000\u001a\u0000\u0007\u0001\u0000\u0000\u0000"+
		"\u0002\u0013\u0001\u0000\u0000\u0000\u0004\u0006\u0003\u0002\u0001\u0000"+
		"\u0005\u0004\u0001\u0000\u0000\u0000\u0006\t\u0001\u0000\u0000\u0000\u0007"+
		"\u0005\u0001\u0000\u0000\u0000\u0007\b\u0001\u0000\u0000\u0000\b\u0001"+
		"\u0001\u0000\u0000\u0000\t\u0007\u0001\u0000\u0000\u0000\n\u000b\u0005"+
		"\u0005\u0000\u0000\u000b\f\u0005\b\u0000\u0000\f\u0014\u0005\b\u0000\u0000"+
		"\r\u0014\u0005\u0001\u0000\u0000\u000e\u0014\u0005\u0002\u0000\u0000\u000f"+
		"\u0014\u0005\u0004\u0000\u0000\u0010\u0014\u0005\u0003\u0000\u0000\u0011"+
		"\u0014\u0005\u0006\u0000\u0000\u0012\u0014\u0005\u0007\u0000\u0000\u0013"+
		"\n\u0001\u0000\u0000\u0000\u0013\r\u0001\u0000\u0000\u0000\u0013\u000e"+
		"\u0001\u0000\u0000\u0000\u0013\u000f\u0001\u0000\u0000\u0000\u0013\u0010"+
		"\u0001\u0000\u0000\u0000\u0013\u0011\u0001\u0000\u0000\u0000\u0013\u0012"+
		"\u0001\u0000\u0000\u0000\u0014\u0003\u0001\u0000\u0000\u0000\u0002\u0007"+
		"\u0013";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}