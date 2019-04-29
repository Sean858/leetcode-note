// Remember the question, and know the thought and mapentry ceilingentry and floorEntry way
class Solution {
    public int oddEvenJumps(int[] A) {
        int len = A.length;
//      Difference between boolean and Boolean!
        boolean[] higher = new boolean[len], lower = new boolean[len];
        TreeMap<Integer, Integer> map = new TreeMap<>();
        // From back to front
        higher[len - 1] = lower[len - 1] = true;
        int res = 1;
        map.put(A[len - 1], len - 1);
        for (int i = len - 2; i >= 0; i--) {
            // Use the treemap to get the higher and lower
            Map.Entry hi = map.ceilingEntry(A[i]), lo = map.floorEntry(A[i]);
            if (hi != null) higher[i] = lower[(int)hi.getValue()];
            if (lo != null) lower[i] = higher[(int)lo.getValue()];
            if (higher[i]) res ++;
            map.put(A[i], i);
        }
        return res;
        
    }
}