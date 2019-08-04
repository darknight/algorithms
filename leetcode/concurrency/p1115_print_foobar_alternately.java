import java.util.concurrent.Semaphore;

class FooBar {
    private int n;
    private Semaphore semaFoo;
    private Semaphore semaBar;

    public FooBar(int n) {
        this.n = n;
        this.semaFoo = new Semaphore(1);
        this.semaBar = new Semaphore(0);
    }

    public void foo(Runnable printFoo) throws InterruptedException {

        for (int i = 0; i < n; i++) {
            semaFoo.acquire();
            // printFoo.run() outputs "foo". Do not change or remove this line.
            printFoo.run();
            semaBar.release();
        }
    }

    public void bar(Runnable printBar) throws InterruptedException {

        for (int i = 0; i < n; i++) {
            semaBar.acquire();
            // printBar.run() outputs "bar". Do not change or remove this line.
            printBar.run();
            semaFoo.release();
        }
    }
}
