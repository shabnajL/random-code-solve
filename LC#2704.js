/**
  * @30 Days of JavaScript
 LeetCode 2704. To Be Or Not To Be
 
 * @param {string} val
 * @return {Object}
 */


var expect = function(val) {
    return {
        toBe: (expect) => {
            const valueType = typeof Val;
            if (val === expect){
                return true;
            }
            else{
                throw new Error ("Not Equal");
            }
        },
        notToBe: (expect) => {
            if (val !== expect){
                return true;
            }
            else{
                throw new Error ("Equal");
            }
        }
    }
    
};

/**
 * expect(5).toBe(5); // true
 * expect(5).notToBe(5); // throws "Equal"
 */
