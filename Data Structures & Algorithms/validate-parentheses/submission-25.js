class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isValid(s) {
        const stack = []
        const pair = {")":"(", "}":"{", "]":"["}

        for(const ch of s){
            if (ch ==="(" || ch === "[" || ch === "{"){
                stack.push(ch);
            }else{
                if (stack.pop() != pair[ch]){
                    return false
                }
            }
        }
        return stack.length === 0;
    }
}
