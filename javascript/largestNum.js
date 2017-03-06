var compare = function(x,y){
	if (x + y > y + x) {
		return -1;
	}
	else{
		return 1;
	}
}
var largestNumber = function(nums){
	var result = '';
	for (var i = 0; i < nums.length; i++) {
		// 字符串到数字：parseInt，parseFloat
		nums[i] = nums[i].toString();
	}
	// debug(typeof(nums[0]))
	nums.sort(compare);
	if (nums[0] == '0') {
		return '0';
	}
	for (prop in nums) {
		if (nums.hasOwnProperty(prop)) {
			result = result + nums[prop];
		}
	}
	return result;
}
debug(largestNumber([12,121]));