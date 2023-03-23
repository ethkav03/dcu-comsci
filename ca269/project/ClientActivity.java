public class ClientActivity implements Activity {
    private String URI;

    ClientActivity (String URI) {
        this.URI = URI;
    }

    public String getURI () {
        return this.URI;
    }
}
