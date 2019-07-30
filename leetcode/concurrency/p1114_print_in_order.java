import java.util.concurrent.Semaphore;

class Foo {

    private Semaphore semaFirst;
    private Semaphore semaSecond;
    private Semaphore semaThird;

    public Foo() {
        semaFirst = new Semaphore(1);
        semaSecond = new Semaphore(0);
        semaThird = new Semaphore(0);
    }

    public void first(Runnable printFirst) throws InterruptedException {

        semaFirst.acquire();
        // printFirst.run() outputs "first". Do not change or remove this line.
        printFirst.run();
        semaSecond.release();
    }

    public void second(Runnable printSecond) throws InterruptedException {

        semaSecond.acquire();
        // printSecond.run() outputs "second". Do not change or remove this line.
        printSecond.run();
        semaThird.release();
    }

    public void third(Runnable printThird) throws InterruptedException {

        semaThird.acquire();
        // printThird.run() outputs "third". Do not change or remove this line.
        printThird.run();
        semaFirst.release();
    }
}