// Generated from draw.g4 by ANTLR 4.13.2
import org.antlr.v4.runtime.tree.ParseTreeVisitor;

/**
 * This interface defines a complete generic visitor for a parse tree produced
 * by {@link drawParser}.
 *
 * @param <T> The return type of the visit operation. Use {@link Void} for
 * operations with no return type.
 */
public interface drawVisitor<T> extends ParseTreeVisitor<T> {
	/**
	 * Visit a parse tree produced by {@link drawParser#prog}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitProg(drawParser.ProgContext ctx);
	/**
	 * Visit a parse tree produced by the {@code init}
	 * labeled alternative in {@link drawParser#stm}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitInit(drawParser.InitContext ctx);
	/**
	 * Visit a parse tree produced by the {@code up}
	 * labeled alternative in {@link drawParser#stm}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitUp(drawParser.UpContext ctx);
	/**
	 * Visit a parse tree produced by the {@code down}
	 * labeled alternative in {@link drawParser#stm}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDown(drawParser.DownContext ctx);
	/**
	 * Visit a parse tree produced by the {@code right}
	 * labeled alternative in {@link drawParser#stm}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitRight(drawParser.RightContext ctx);
	/**
	 * Visit a parse tree produced by the {@code left}
	 * labeled alternative in {@link drawParser#stm}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitLeft(drawParser.LeftContext ctx);
	/**
	 * Visit a parse tree produced by the {@code draw}
	 * labeled alternative in {@link drawParser#stm}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDraw(drawParser.DrawContext ctx);
	/**
	 * Visit a parse tree produced by the {@code display}
	 * labeled alternative in {@link drawParser#stm}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDisplay(drawParser.DisplayContext ctx);
}