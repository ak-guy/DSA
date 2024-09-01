package Misc;

import java.util.*;

class IntStrTuple implements Comparable<IntStrTuple>{
    private final Integer time;
    private final String eventName;

    public IntStrTuple(int time, String eventName) {
        this.time = time;
        this.eventName = eventName;
    }

    public int getTime() {
        return time;
    }

    public String getEventName() {
        return eventName;
    }

    @Override
    public String toString() {
        return "(" + time + ", " + eventName + ")";
    }

    @Override
    public int compareTo(IntStrTuple other) {
        int numCompare = this.time.compareTo(other.time);
        if (numCompare != 0) {
            return numCompare;
        }
        int x = this.eventName.equals("end") ? 1 : 0;
        return x;
    }
}

class Solution {
    int minMeetingRooms(int[][] intervals) {
        int roomRequired = 0;
        int currentNumberOfRooms = 0;
        PriorityQueue<IntStrTuple> pq = new PriorityQueue<>();

        for (int[] interval : intervals) {
            pq.add(new IntStrTuple(interval[0], "start"));
            pq.add(new IntStrTuple(interval[1]+1, "end"));
        }

        while (!pq.isEmpty()) {
            IntStrTuple firstMeeting = pq.poll();
            System.out.println(firstMeeting);
            if (firstMeeting.getEventName() == "start") {
                currentNumberOfRooms++;
                roomRequired = Math.max(roomRequired, currentNumberOfRooms);
            }else{
                currentNumberOfRooms--;
            }
        }

        return roomRequired;
    }
}
