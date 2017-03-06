class Solution{

	public int kthLargestElement(int k , int[] nums){
		int result = quickSort(k,nums,0,nums.length - 1);
		return result;
	}

	public Integer quickSort(int k,int[] nums,int left,int right){
		if (left > right) {
			return null;
		}
		int p = left;
		int q = right;
		int key = nums[left];
		while (p < q) {
			while (p < q && nums[q] <= key) {
				q--;
			}
			nums[p] = nums[q];
			while(p < q && nums[p] >= key){
				p++;
			}
			nums[q] = nums[p];
		}
		nums[p] = key;	
		if (p < k - 1) {
			return quickSort(k,nums,p + 1,right);
		}
		else if (p == k - 1) {
			return nums[p];
		}
		else{
			return quickSort(k,nums,left,p - 1);
		}
	}
}; 

public class 第k大数 {
	public static void main(String[] args) {
		Solution solution = new Solution();
		int arry[] = {1,2,3,8,5,3};
		int s = solution.kthLargestElement(5,arry);
		System.out.println(s);
	}
}
