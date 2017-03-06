var insert = function(intervals, newInterval) {
	var result = [];
    intervals.push(newInterval);
    intervals.sort(function(a,b){return a.start - b.start});
    debug(intervals)
    result.push(intervals[0])
    for (prop in intervals) {
    	debug(result)
    	debug(prop)
    	if (intervals.hasOwnProperty(prop)) {
    		if (prop >= 1) {
    			if (intervals[prop].start <= result[result.length - 1].end) {

    				result[result.length - 1].end = Math.max(result[result.length - 1].end,intervals[prop].end);
    			}
    			else{
    				result.push(intervals[prop]);
    			}
    		}
    	}
    }
    return result;
};

debug(insert([[1,5]],[0,3]))