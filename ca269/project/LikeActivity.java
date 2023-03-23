public class LikeActivity extends ClientActivity {
    private String summary;
    private Person actor;
    private StreamObject streamObject;

    LikeActivity (String URI, String summary, Person actor, StreamObject streamObject) {
        super(URI);
        setSummary(summary);
        setActor(actor);
        setStreamObject(streamObject);
    }

    // setters

    public void setSummary (String summary) {
        this.summary = summary;
    }

    public void setActor (Person actor) {
        this.actor = actor;
    }

    public void setStreamObject (StreamObject streamObject) {
        this.streamObject = streamObject;
    }

    // getters

    public String getSummary () {
        return this.summary;
    }

    public Person getActor () {
        return this.actor;
    }

    public StreamObject getStreamObject () {
        return this.streamObject;
    }

    public String toString () {
        return this.getStreamObject().getName() + " was liked by " + this.getActor().getName();
    }
}