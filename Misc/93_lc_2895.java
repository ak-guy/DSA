package Misc;

/*
 * 2895. Minimum Processing Time
 */

import java.util.*;
class Solution {
    public int minProcessingTime(List<Integer> processorTime, List<Integer> tasks) {
        int res = 0;
        Collections.sort(tasks);
        Collections.sort(processorTime);
        
        int startingIndex = 0;
        int endingIndex = 3;
        for (int i=processorTime.size()-1; i>= 0; i--) {
            int dummyRes = 0;
            int currentProcessorTime = processorTime.get(i);
            for (int j=startingIndex; j<=endingIndex; j++) {
                dummyRes = Math.max(dummyRes, currentProcessorTime + tasks.get(j));
            }
            startingIndex += 4;
            endingIndex += 4;
            res = Math.max(res, dummyRes);
        }

        return res;
    }
}


class Dummy {
    
}
