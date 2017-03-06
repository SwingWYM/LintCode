class Solution {
	public int hashCode(char[] key,int HASH_SIZE){
		long temp;
		long sum = 0;
		long pow = 1;
		for (int i = key.length - 1; i >= 0; i -- ) {
			temp = ((int)key[i] * pow) % HASH_SIZE;
			sum = (sum + temp) % HASH_SIZE;
			pow = (pow * 33) % HASH_SIZE;

		}

		return (int)(sum % HASH_SIZE);
	}
};