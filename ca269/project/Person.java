import java.util.ArrayList;
import java.util.List;

public class Person extends ClientApp {
    private String URI;
    private String name;
    private String preferredUsername;
    private String summary;
    private List<Person> followers;
    private List<Person> following;
    private List<Person> liked;

    Person (String URI, String name, String preferredUsername, String summary) {
        setURI(URI);
        setName(name);
        setPreferredUsername(preferredUsername);
        setSummary(summary);
        followers = new ArrayList<>();
        following = new ArrayList<>();
        liked = new ArrayList<>();
    }

    public void setURI (String URI) {
        this.URI = URI;
    }

    public void setName (String name) {
        this.name = name;
    }

    public void setPreferredUsername (String preferredUsername) {
        this.preferredUsername = preferredUsername;
    }

    public void setSummary (String summary) {
        this.summary = summary;
    }

    public String getURI () {
        return this.URI;
    }

    public String getName () {
        return this.name;
    }

    public String getPreferredUsername () {
        return this.preferredUsername;
    }

    public String getSummary () {
        return this.summary;
    }

    public List<Person> getFollowers () {
        return this.followers;
    }

    public List<Person> getFollowing () {
        return this.following;
    }

    public List<Person> getLiked () {
        return this.liked;
    }

    public String toString () {
        return "- URI: " + this.getURI() + "\n- Name: " + this.getName() + "\n";
    }
}