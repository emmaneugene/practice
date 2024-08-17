package algos.leetcode.easy;
// Problem: https://leetcode.com/problems/binary-search/
// Time complexity: O(log(n))
// Space complexity: NA


class BinarySearch {
    public static int search(int[] nums, int target) {
        int start = 0;
        int end = nums.length;
        int mid;

        while (start < end) {
            mid = start + (end - start) / 2;

            if (target == nums[mid]) {
                return mid;
            } else if (target < nums[mid]) {
                end = mid;
            } else {
                start = mid + 1;
            }
        }

        return -1;
    }

    public static int search2(int[] nums, int target) {
        int start = 0;
        int end = nums.length - 1;
        int mid;

        while (start <= end) {
            mid = start + (end - start) / 2;

            if (target == nums[mid]) {
                return mid;
            } else if (target < nums[mid]) {
                end = mid - 1;
            } else {
                start = mid + 1;
            }
        }

        return -1;
    }


    public static void main(String[] args) {
        System.out.println("Half open search");
        System.out.println(search(new int[]{-1, 0, 3, 4, 9, 12}, 9)); // Expected: 4
        System.out.println(search(new int[]{-1, 0, 3, 4, 9, 12}, 2)); // Expected: -1
        System.out.println(search(new int[]{-1, 0, 3}, 0)); // Expected: 1
        System.out.println(search(new int[]{-1, 0}, -1)); // Expected: 0
        System.out.println(search(new int[]{-1, 0}, 0)); // Expected: 1

        System.out.println("Inclusive search");
        System.out.println(search2(new int[]{-1, 0, 3, 4, 9, 12}, 9)); // Expected: 4
        System.out.println(search2(new int[]{-1, 0, 3, 4, 9, 12}, 2)); // Expected: -1
        System.out.println(search2(new int[]{-1, 0, 3}, 0)); // Expected: 1
        System.out.println(search2(new int[]{-1, 0}, -1)); // Expected: 0
        System.out.println(search2(new int[]{-1, 0}, 0)); // Expected: 1
    }
}
