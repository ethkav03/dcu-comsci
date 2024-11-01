/**
 * class PublishedBook is child of PunlishedBook
 * @see Book
 * @see PublishedBook
 */
public class ReadBook extends PublishedBook{
    /**
     * attributes of PublishedBook
     * inherits title, author, genre, publishedDate and medium from PublishedBook
     * aswell as associated getters and setters
     */
    private int readDate;
    private BookRating rating;

    /**
     * constructor for ReadBook
     * @param title
     * @param author
     * @param genre
     * @param publishedDate
     * @param readDate
     * @param medium
     * @param rating
     */
    ReadBook (String title, String author, BookGenre genre, int publishedDate, int readDate, BookMedium medium, BookRating rating) {
        super(title, author, genre, publishedDate, medium);
        setReadDate(readDate);
        setBookRating(rating);
    }

    /**
     * setter for readDate
     * @param readDate int
     */
    public void setReadDate(int readDate) {
        this.readDate = readDate;
    }

    /**
     * setter for rating
     * @param rating BookRating
     */
    public void setBookRating(BookRating rating) {
        this.rating = rating;
    }

    /**
     * getter for readdate
     * @return int
     */
    public int getReadDate() {
        return this.readDate;
    }

    /**
     * getter for rating
     * @return BookRating
     */
    public BookRating getRating() {
        return this.rating;
    }

    /**
     * converts ReadBook to a string
     */
    public String toString() {
        return this.getTitle() + " by " + this.getAuthor() + " (" + this.getPublishedDate() + ") - read in " + this.getReadDate() + ", rated " + (BookRating.valueOf("" + this.getRating()).ordinal() + 1) + "/5";
    }
}