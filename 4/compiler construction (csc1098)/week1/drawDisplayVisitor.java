public class drawDisplayVisitor extends drawBaseVisitor<Integer> {
    Boolean [][] display;
    int xSize, ySize;
    int x = 0, y = 0;

    @Override
    public Integer visitInit(drawParser.InitContext ctx) {
        xSize = Integer.valueOf(ctx.NUMBER(0).getText());
        ySize = Integer.valueOf(ctx.NUMBER(1).getText());

        display = new Boolean[xSize][ySize];

        for (int i = 0; i < xSize; i++) {
            for (int j = 0; j < ySize; j++) {
                display[i][j] = false;
            }
        }
        return 0;
    }
}