import java.util.Stack;
import java.util.Queue;
import java.util.LinkedList;
import java.util.Map;
import java.util.LinkedHashMap;

class Item {
    private final String name;
    private final double price;

    Item (String name, double d) {
        this.name = name;
        this.price = d;
    }

    public String getName () {
        return this.name;
    }

    public double getPrice () {
        return this.price;
    }
}

class Basket {
    private final Stack<Item> basket;

    Basket() {
        this.basket = new Stack<>();
    }

    public void addItem(Item item) {
        this.basket.push(item);
    }

    public Item removeItem() {
        if (!this.basket.empty()) {
            return this.basket.pop();
        }
        return null;
    }

    public String toString() {
        return "basket:" + this.basket.toString();
    }
}

class Checkout {
    private final Queue<Item> checkout;

    Checkout(Basket basket) {
        this.checkout = new LinkedList<Item>();
        Item item = basket.removeItem();
        while (item != null) {
            this.addItem(item);
            item = basket.removeItem();
        }
    }

    public void addItem(Item item) {
        this.checkout.add(item);
    }

    public Item removeItem() {
        if (!this.checkout.isEmpty()) {
            return this.checkout.remove();
        }
        return null;
    }
    

    public String toString() {
        return "checkout:" + this.checkout.toString();
    }
}

class Bill {
    private final Map<String,Integer> basket;
    private double price;

    Bill(Checkout checkout) {
        // TODO - initialise Map, set price, bill items from checkout
        this.basket = new LinkedHashMap<String, Integer>();
        this.price = 0;
        if (checkout != null) {
            Item item = checkout.removeItem();
            while (item != null) {
                this.billItem(item);
                item = checkout.removeItem();
            }
        }
    }

    public void billItem(Item item) {
        // TODO - put item in map, keep count of same items being billed
        // Note that the Map is from String to Integer
        // Items have names as Strings and count of items is an integer
        if (this.basket.containsKey(item.getName())) {
            this.basket.put(item.getName(), this.basket.get(item.getName()) + 1);
        }
        else {
            this.basket.put(item.getName(), 1);
        }
        this.price += item.getPrice();
    }

    public double getTotal() {
        return this.price;
    }

    public String toString() {
        String output = "";
        for(String item: this.basket.keySet()) {
            output += item + " (" + this.basket.get(item) + "nos)\n";
        }
        return output + "total: " + this.price;
    }
}

public class ShopInventory2 {
    public static void main(String[] args) {
        Basket basket = new Basket();
        loadBasket(basket);
        // System.out.println(basket); // for DEBUG
        Checkout checkout = new Checkout(basket);
        // System.out.println(checkout); // for DEBUG
        Bill bill = new Bill(checkout);
        System.out.println(bill);
    }

    static void loadBasket(Basket basket) {
        basket.addItem(new Item("Twinings Earl Grey Tea", 4.50));
        basket.addItem(new Item("Folans Orange Marmalade", 4.00));
        basket.addItem(new Item("Free-range Eggs", 3.35));
        basket.addItem(new Item("Brennan's Bread", 2.15));
        basket.addItem(new Item("Ferrero Rocher", 7.00));
        basket.addItem(new Item("Ferrero Rocher", 7.00));
    }
}