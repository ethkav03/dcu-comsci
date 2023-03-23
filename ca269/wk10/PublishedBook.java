/**
 * class PublishedBook is parent class of ReadBook
 * class PublishedBook is child of Book
 * @see Book
 * @see ReadBook
 */
public class PublishedBook extends Book{
    /**
     * attributes of PublishedBook
     * inherits title, author and genre from Book
     * aswell as associated getters and setters
     */
    private int publishedDate;
    private BookMedium medium;

    /**
     * Constructor of PublishedBook
     * @param title
     * @param author
     * @param genre
     * @param publishedDate
     * @param medium
     */
    PublishedBook (String title, String author, BookGenre genre, int publishedDate, BookMedium medium) {
        super(title, author, genre);
        setPublishedDate(publishedDate);
        setBookMedium(medium);
    }

    /**
     * setter for publishedDate
     * @param publishedDate int
     */
    public void setPublishedDate(int publishedDate) {
        this.publishedDate = publishedDate;
    }

    /**
     * setter for medium
     * @param medium BookMedium
     */
    public void setBookMedium(BookMedium medium) {
        this.medium = medium;
    }

    /**
     * getter for publishedDate
     * @return int
     */
    public int getPublishedDate() {
        return this.publishedDate;
    }

    /**
     * getter for medium
     * @return BookMedium
     */
    public BookMedium getMedium() {
        return this.medium;
    }

    /**
     * converts PublishedBook to a string
     */
    public String toString() {
        return this.getTitle() + " by " + this.getAuthor() + " (" + this.getPublishedDate() + ")";
    }
}