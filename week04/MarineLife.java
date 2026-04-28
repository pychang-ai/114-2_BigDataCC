package week04;

class MarineLife {
    void breathe() {
        System.out.println("breathing...");
    }
}

class Fish extends MarineLife {
    void swim() {
        System.out.println("Fish is swimming...");
    }
    public static void main(String[] args) {

        Fish f = new Fish();

        f.breathe(); // 從 MarineLife 繼承來的
        f.swim();    // Fish 自己的功能
    }
}