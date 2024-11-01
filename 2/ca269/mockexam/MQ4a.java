class Apple { }
class AppleFactory extends Factory<Apple> { }

class Orange { }
class OrangeFactory extends Factory<Orange> { }

class Lemon { }
class LemonFactory extends Factory<Lemon> {
    @Override
    public void setItem (Lemon item) {
        if (this.item == null) {
            this.item = item;
        }
    }

    public void removeItem () {
        this.item = null;
    }
}

class Factory<T> {
    T item;
    
    public void setItem (T item) {
        this.item = item;
    }

    public T getItem () {
        return this.item;
    }
}