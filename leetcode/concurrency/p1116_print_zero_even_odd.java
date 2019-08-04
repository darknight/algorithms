import java.util.function.IntConsumer;
import java.util.concurrent.Semaphore;

class ZeroEvenOdd {
    private int n;
    private int endOdd;
    private int endEven;
    private Semaphore semaZero;
    private Semaphore semaOdd;
    private Semaphore semaEven;

    public ZeroEvenOdd(int n) {
        this.n = n;
        if (n % 2 == 0){
            this.endEven = n;
            this.endOdd = n - 1;
        } else {
            this.endEven = n - 1;
            this.endOdd = n;
        }
        this.semaZero = new Semaphore(1);
        this.semaOdd = new Semaphore(0);
        this.semaEven = new Semaphore(0);
    }

    // printNumber.accept(x) outputs "x", where x is an integer.
    public void zero(IntConsumer printNumber) throws InterruptedException {
        for (int i = 1; i <= n; i++) {
            semaZero.acquire();
            printNumber.accept(0);
            if (i % 2 == 0) {
                semaEven.release();
            } else {
                semaOdd.release();
            }
        }
    }

    public void even(IntConsumer printNumber) throws InterruptedException {
        for (int i = 2; i <= endEven; i += 2) {
            semaEven.acquire();
            printNumber.accept(i);
            semaZero.release();
        }
    }

    public void odd(IntConsumer printNumber) throws InterruptedException {
        for (int i = 1; i <= endOdd; i += 2) {
            semaOdd.acquire();
            printNumber.accept(i);
            semaZero.release();
        }

    }
}
