import java.time.LocalDate;

public class StreamObject {
    private String URI;
    private String attachment;
    private String attributedTo;
    private Audience audience;
    private int likes;
    private int shares;
    private String content;
    private String name;
    private LocalDate published;
    private LocalDate deleted;

    StreamObject (String URI, String attachment, String attributedTo, Audience audience, String content, String name) {
        setURI(URI);
        setAttachment(attachment);
        setAttributedTo(attributedTo);
        setAudience(audience);
        this.likes = 0;
        this.shares = 0;
        setContent(content);
        setName(name);
        this.published = java.time.LocalDate.now();
    }

    // setters
    public void setURI (String URI) {
        this.URI = URI;
    }

    public void setAttachment (String attachment) {
        this.attachment = attachment;
    }

    public void setAttributedTo (String attributedTo) {
        this.attributedTo = attributedTo;
    }

    public void setContent (String content) {
        this.content = content;
    }

    public void setName (String name) {
        this.name = name;
    }

    public void setAudience (Audience audience) {
        this.audience = audience;
    }

    //getters
    public String getURI () {
        return this.URI;
    };
    public String getAttachment () {
        return this.attachment;
    };

    public String getAttributedTo () {
        return this.attributedTo;
    };

    public Audience getAudience () {
        return this.audience;
    };

    public int getLikes () {
        return this.likes;
    };

    public int getShares () {
        return this.shares;
    };

    public String getContent () {
        return this.content;
    };

    public String getName () {
        return this.name;
    };

    public LocalDate getPublished () {
        return this.published;
    };

    public LocalDate getDeleted () {
        return this.deleted;
    };

    public String toString () {
        return this.getName() + " was created.";
    }
}

enum Audience {
    GLOBAL,
    LOCAL,
}