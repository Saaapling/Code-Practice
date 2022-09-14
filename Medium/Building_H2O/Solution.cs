using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Threading;

namespace Practice_Code.Building_H2O
{
    public class H2O
    {
        /*
         * Problem: https://leetcode.com/problems/building-h2o/
         * Time Taken: 30 (mostly research, some interrupted time inbetween)
         * References:
         *      - https://docs.microsoft.com/en-us/dotnet/api/system.threading.barrier?redirectedfrom=MSDN&view=net-6.0
         *      - https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Phaser.html
         * Comments: There are many ways to do this without a barrier/phaser, but the question itself is
         *      confusing..., and may options without a barrier can get restrictive
         */

        private static Semaphore oxygen = new Semaphore(1, 1);
        private static Semaphore hydrogen = new Semaphore(2, 2);
        private static Barrier shared = new Barrier(3);


        public H2O()
        {

        }

        public void Hydrogen(Action releaseHydrogen)
        {
            hydrogen.WaitOne();
            shared.SignalAndWait();

            // releaseHydrogen() outputs "H". Do not change or remove this line.
            releaseHydrogen();

            hydrogen.Release();
        }

        public void Oxygen(Action releaseOxygen)
        {
            oxygen.WaitOne();
            shared.SignalAndWait();

            // releaseOxygen() outputs "O". Do not change or remove this line.
            releaseOxygen();

            oxygen.Release();
        }
    }
}
