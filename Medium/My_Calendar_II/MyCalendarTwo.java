package Medium.My_Calendar_II;

import java.util.ArrayList;

public class MyCalendarTwo {

    /*
        Problem: https://leetcode.com/problems/my-calendar-ii/
        Time Taken: 60 min
        Considerations:
        - Improvements to existing method: There is the consideration that, since we only care about
            triple bookings (3), we can just 2 lists, one of bookings, and one of overlaps. If a new
            booking intersects with an overlap, return false. I *don't* like this method because it
            only works for 3's. The current method works for any number.
        Better method: Use a treemap solution, much more elegant. This solution works because while
            the TreeMap sum is always 0, if it equals 3 (or any other specified number) mid-sum, it
            indicates a triple booking at the specified time.

            TreeMap<Integer, Integer> delta;

            public MyCalendarTwo() {
                delta = new TreeMap();
            }

            public boolean book(int start, int end) {
                delta.put(start, delta.getOrDefault(start, 0) + 1);
                delta.put(end, delta.getOrDefault(end, 0) - 1);

                int active = 0;
                for (int d: delta.values()) {
                    active += d;
                    if (active >= 3) {
                        delta.put(start, delta.get(start) - 1);
                        delta.put(end, delta.get(end) + 1);
                        if (delta.get(start) == 0)
                            delta.remove(start);
                        return false;
                    }
                }
                return true;
            }
     */

    class TimePair {
        int time;
        int count;

        public TimePair(int x, int y){
            time = x;
            count = y;
        }
    };

    private ArrayList<TimePair> time_list = new ArrayList<TimePair>();

    public MyCalendarTwo() {
        time_list.add(new TimePair(0,0));
    }

    private ArrayList<TimePair> deep_copy(ArrayList<TimePair> original){
        ArrayList<TimePair> new_copy = new ArrayList<>();
        for (TimePair curr : original){
            new_copy.add(new TimePair(curr.time, curr.count));
        }

        return new_copy;
    }

    public boolean book(int start, int end) {
        ArrayList<TimePair> time_list = deep_copy(this.time_list);

        int index = 0;
        boolean found = false;
        for (; index < time_list.size(); index++){
            TimePair time_pair = time_list.get(index);
            int start_time = time_pair.time;
            if (start > start_time){
                continue;
            } else if (start == start_time) {
                // Update existing entry in list
                if (time_pair.count < 2){
                    time_pair.count += 1;
                }else{
                    return false;
                }
                index += 1;
                found = true;
                break;
            } else{
                // Insert a new time into list
                TimePair prev_pair = time_list.get((index - 1));
                if (prev_pair.count < 2){
                    time_list.add(index, new TimePair(start, prev_pair.count + 1));
                    index += 1;
                }else {
                    return false;
                }
                found = true;
                break;
            }
        }

        if (!found){
            time_list.add(new TimePair(start, 1));
            time_list.add(new TimePair(end, 0));
            this.time_list = time_list;
            return true;
        }

        found = false;
        for (; index < time_list.size(); index++){
            TimePair time_pair = time_list.get(index);
            int start_time = time_pair.time;
            if (end > start_time){
                // Update existing entry in list
                if (time_pair.count < 2){
                    time_pair.count += 1;
                }else{
                    return false;
                }
            } else if (end == start_time) {
                found = true;
                break;
            } else{
                // Insert a new time into list
                TimePair prev_pair = time_list.get((index - 1));
                time_list.add(index, new TimePair(end, prev_pair.count - 1));
                found = true;
                break;
            }
        }

        if (!found){
            time_list.add(new TimePair(end, 0));
        }

        this.time_list = time_list;
        return true;
    }

    public void print(){
        for (TimePair curr : time_list){
            System.out.print("[" + curr.time + ", " + curr.count + "], ");
        }
        System.out.println();
    }

    public static void main(String[]args){
        MyCalendarTwo test = new MyCalendarTwo();
        System.out.println(test.book(24,40));
        test.print();
        System.out.println(test.book(43,50));
        test.print();
        System.out.println(test.book(27,43));
        test.print();
        System.out.println(test.book(5,21));
        test.print();
        System.out.println(test.book(30,40));
        test.print();
        System.out.println(test.book(14,29));
        test.print();
        System.out.println(test.book(3,19));
        test.print();
        System.out.println(test.book(3,14));
        test.print();
        System.out.println(test.book(25,39));
        test.print();
        System.out.println(test.book(6,19));
        test.print();
    }

    /*
    ["MyCalendarTwo","book","book","book","book","book","book","book","book","book","book"]
[[],[24,40],[43,50],[27,43],[5,21],[30,40],[14,29],[3,19],[3,14],[25,39],[6,19]]

     */

}
