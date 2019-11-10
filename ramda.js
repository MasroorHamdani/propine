/*
Question 3 - Maintenance(Optional)

For the most of your career, you will spend more time reading code than writing it. Frequently, you will come into an existing codebase and be asked to change it.

Add a retry function to Ramda such that it attempts to get a true response from the function at most N times..

Arguments
func (Function): The function to invoke. It should return a true or false.
[wait=0] (Number): The number of milliseconds to delay.
[options={}] (Object): The options object
[options.max] (Number): Optional. The maximum number of times to invoke the function to get a success response. If null it will retry forever.
Returns
(Boolean): Returns true if the func returns a success response, false otherwise.
*/

let f = () => {
    retValue = Math.random() >= 0.5;
    return retValue; // => true or false
};
var callCount = 1;

let retry = (wait, options) => {
    count = null;
    returnValue = false;
    if (options && options['max']) {
        count = options['max']
    }
    setInterval(function () {
        if((count !== null && callCount <= count && !returnValue) ||
            (count === null && !returnValue)) {
            returnValue = f();
            callCount += 1;
        }
    }, wait);
}

// retry with max value as 2 - this function will at max try twice to get the true value with an interval of 1000 milliseconds.
retry(1000, {'max':2} );
// retry with null value - this function will keep calling till inner function returns true with an interval of 1000 milliseconds.
retry(1000, {} );