public class Book {
    private String title;
    private String author;
    private int publishedDate;
    private int readDate;
    private BookMedium medium;
    private BookGenre genre;
    private BookRating rating;

    Book (String title, String author, BookGenre genre) {
        setTitle(title);
        setAuthor(author);
        setBookGenre(genre);
    }

    Book (String title, String author, BookGenre genre, int publishedDate) {
        setTitle(title);
        setAuthor(author);
        setBookGenre(genre);
        setPublishedDate(publishedDate);
    }

    Book (String title, String author, BookGenre genre, int publishedDate, int readDate, BookMedium medium, BookRating rating) {
        setTitle(title);
        setAuthor(author);
        setBookGenre(genre);
        setPublishedDate(publishedDate);
        setReadDate(readDate);
        setBookMedium(medium);
        setBookRating(rating);
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public void setAuthor(String author) {
        this.author = author;
    }

    public void setPublishedDate(int publishedDate) {
        this.publishedDate = publishedDate;
    }

    public void setReadDate(int readDate) {
        this.readDate = readDate;
    }

    public void setBookMedium(BookMedium medium) {
        this.medium = medium;
    }

    public void setBookGenre(BookGenre genre) {
        this.genre = genre;
    }

    public void setBookRating(BookRating rating) {
        this.rating = rating;
    }

    public String getTitle() {
        return this.title;
    }

    public String getAuthor() {
        return this.author;
    }

    public int getPublishedDate() {
        return this.publishedDate;
    }

    public int getReadDate() {
        return this.readDate;
    }

    public BookMedium getMedium() {
        return this.medium;
    }

    public BookGenre getGenre() {
        return this.genre;
    }

    public BookRating getRating() {
        return this.rating;
    }

    public String toString() {
        if (this.readDate > 0) {
            return this.title + " by " + this.author + " (" + this.publishedDate + ") - read in " + this.readDate + ", rated " + (BookRating.valueOf("" + this.rating).ordinal() + 1) + "/5";
        } else if (this.publishedDate > 0) {
            return this.title + " by " + this.author + " (" + this.publishedDate + ")";
        } else {
            return this.title + " by " + this.author;
        }
    }

    public static void main(String args[]) {
        Book b1 = new Book("Children of Time", "Adrian Tchaikovsky", BookGenre.Fiction);
        System.out.println(b1);
        Book b2 = new Book("The Fifth Season", "N. K. Jemesin", BookGenre.Fiction, 2015);
        System.out.println(b2);
        Book b3 = new Book("Perdido Street Station", "China Mieville", BookGenre.Fiction, 2000, 2020, BookMedium.EBook, BookRating.Rating5);
        System.out.println(b3);

        System.out.println(b1.getTitle());
        System.out.println(b1.getAuthor());
        System.out.println(b1.getGenre());
        System.out.println(b2.getPublishedDate());
        System.out.println(b3.getReadDate());
        System.out.println(b3.getMedium());
        System.out.println(b3.getRating());
    }
}

enum BookMedium {
    PhysicalBook,
    EBook,
    AudioBook
}

enum BookGenre {
    Fiction,
    Nonfiction
}

enum BookRating {
    Rating1,
    Rating2,
    Rating3,
    Rating4,
    Rating5
}