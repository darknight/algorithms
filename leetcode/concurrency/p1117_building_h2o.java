import java.util.concurrent.BrokenBarrierException;
import java.util.concurrent.CyclicBarrier;
import java.util.concurrent.Semaphore;

class H2O {

    private CyclicBarrier barrier;
    private Semaphore semaHyd;
    private Semaphore semaOxy;

    public H2O() {
        this.semaHyd = new Semaphore(2);
        this.semaOxy = new Semaphore(1);
        this.barrier = new CyclicBarrier(3);
    }

    public void hydrogen(Runnable releaseHydrogen) throws InterruptedException {
        semaHyd.acquire();
        // releaseHydrogen.run() outputs "H". Do not change or remove this line.
        releaseHydrogen.run();
        try {
            barrier.await();
            System.out.println("");
        } catch (BrokenBarrierException e) {}
    }

    public void oxygen(Runnable releaseOxygen) throws InterruptedException {
        semaOxy.acquire();
        // releaseOxygen.run() outputs "O". Do not change or remove this line.
        releaseOxygen.run();
        try {
            barrier.await();
            System.out.println("");
        } catch (BrokenBarrierException e) {}
        semaOxy.release(1);
        semaHyd.release(2);
    }
}
