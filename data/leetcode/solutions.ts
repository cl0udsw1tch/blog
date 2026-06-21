import type MetaData from "@/components/MetaData";

// prism.ts
import Prism from "prismjs";
import "prismjs/components/prism-python";
export default Prism




export type LeetCodeData = MetaData


export const solutions: Array<LeetCodeData> = [
    {
        slug: "1-two-sum",
        class: "leetcode",
        title: "1-two-sum",
        date: "",
        category: "hash-map",
        description: "Find two indices whose values add up to a given target.",
        file: "1-two-sum.md",
        type: "py"
    },
    {
        slug: "10-regular-expression-matching",
        class: "leetcode",
        title: "10-regular-expression-matching",
        date: "",
        category: "dynamic-programming",
        description: "Determine whether a string matches a pattern containing '.' and '*'.",
        file: "10-regular-expression-matching.md",
        type: "py"
    },
    {
        slug: "100-same-tree",
        class: "leetcode",
        title: "100-same-tree",
        date: "",
        category: "tree",
        description: "Check whether two binary trees are structurally identical with equal node values.",
        file: "100-same-tree.md",
        type: "py"
    },
    {
        slug: "1008-binary-tree-cameras",
        class: "leetcode",
        title: "1008-binary-tree-cameras",
        date: "",
        category: "tree-dp",
        description: "Place the minimum number of cameras to monitor every node in a binary tree.",
        file: "1008-binary-tree-cameras.md",
        type: "py"
    },
    {
        slug: "101-symmetric-tree",
        class: "leetcode",
        title: "101-symmetric-tree",
        date: "",
        category: "tree",
        description: "Determine whether a binary tree is symmetric around its center.",
        file: "101-symmetric-tree.md",
        type: "py"
    },
    {
        slug: "1013-fibonacci-number",
        class: "leetcode",
        title: "1013-fibonacci-number",
        date: "",
        category: "dynamic-programming",
        description: "Compute the nth Fibonacci number using the recurrence relation.",
        file: "1013-fibonacci-number.md",
        type: "py"
    },
    {
        slug: "102-binary-tree-level-order-traversal",
        class: "leetcode",
        title: "102-binary-tree-level-order-traversal",
        date: "",
        category: "bfs",
        description: "Return the values of a binary tree level by level.",
        file: "102-binary-tree-level-order-traversal.md",
        type: "py"
    },
    {
        slug: "1025-minimum-cost-for-tickets",
        class: "leetcode",
        title: "1025-minimum-cost-for-tickets",
        date: "",
        category: "dynamic-programming",
        description: "Find the minimum travel cost using ticket passes of different durations.",
        file: "1025-minimum-cost-for-tickets.md",
        type: "py"
    },
    {
        slug: "1028-interval-list-intersections",
        class: "leetcode",
        title: "1028-interval-list-intersections",
        date: "",
        category: "two-pointers",
        description: "Find all intersections between two sorted interval lists.",
        file: "1028-interval-list-intersections.md",
        type: "py"
    },
    {
        slug: "103-binary-tree-zigzag-level-order-traversal",
        class: "leetcode",
        title: "103-binary-tree-zigzag-level-order-traversal",
        date: "",
        category: "bfs",
        description: "Traverse a binary tree level by level while alternating traversal direction.",
        file: "103-binary-tree-zigzag-level-order-traversal.md",
        type: "py"
    },
    {
        slug: "104-maximum-depth-of-binary-tree",
        class: "leetcode",
        title: "104-maximum-depth-of-binary-tree",
        date: "",
        category: "tree",
        description: "Compute the maximum depth of a binary tree.",
        file: "104-maximum-depth-of-binary-tree.md",
        type: "py"
    },
    {
        slug: "1042-minimum-cost-to-merge-stones",
        class: "leetcode",
        title: "1042-minimum-cost-to-merge-stones",
        date: "",
        category: "dynamic-programming",
        description: "Determine the minimum cost required to merge piles of stones under given rules.",
        file: "1042-minimum-cost-to-merge-stones.md",
        type: "py"
    },
    {
        slug: "105-construct-binary-tree-from-preorder-and-inorder-traversal",
        class: "leetcode",
        title: "105-construct-binary-tree-from-preorder-and-inorder-traversal",
        date: "",
        category: "tree",
        description: "Reconstruct a binary tree from preorder and inorder traversals.",
        file: "105-construct-binary-tree-from-preorder-and-inorder-traversal.md",
        type: "py"
    },
    {
        slug: "1057-numbers-with-repeated-digits",
        class: "leetcode",
        title: "1057-numbers-with-repeated-digits",
        date: "",
        category: "digit-dp",
        description: "Count numbers up to a limit that contain repeated digits.",
        file: "1057-numbers-with-repeated-digits.md",
        type: "py"
    },
    {
        slug: "106-construct-binary-tree-from-inorder-and-postorder-traversal",
        class: "leetcode",
        title: "106-construct-binary-tree-from-inorder-and-postorder-traversal",
        date: "",
        category: "tree",
        description: "Reconstruct a binary tree from inorder and postorder traversals.",
        file: "106-construct-binary-tree-from-inorder-and-postorder-traversal.md",
        type: "py"
    },
    {
        slug: "108-convert-sorted-array-to-binary-search-tree",
        class: "leetcode",
        title: "108-convert-sorted-array-to-binary-search-tree",
        date: "",
        category: "tree",
        description: "Convert a sorted array into a height-balanced binary search tree.",
        file: "108-convert-sorted-array-to-binary-search-tree.md",
        type: "py"
    },
    {
        slug: "11-container-with-most-water",
        class: "leetcode",
        title: "11-container-with-most-water",
        date: "",
        category: "two-pointers",
        description: "Find the maximum amount of water that can be contained between two lines.",
        file: "11-container-with-most-water.md",
        type: "py"
    },
    {
        slug: "1111-minimum-score-triangulation-of-polygon",
        class: "leetcode",
        title: "1111-minimum-score-triangulation-of-polygon",
        date: "",
        category: "dynamic-programming",
        description: "Compute the minimum triangulation score of a polygon.",
        file: "1111-minimum-score-triangulation-of-polygon.md",
        type: "py"
    },
    {
        slug: "112-path-sum",
        class: "leetcode",
        title: "112-path-sum",
        date: "",
        category: "tree",
        description: "Determine whether a root-to-leaf path sums to a target value.",
        file: "112-path-sum.md",
        type: "py"
    },
    {
        slug: "1130-last-stone-weight-ii",
        class: "leetcode",
        title: "1130-last-stone-weight-ii",
        date: "",
        category: "dynamic-programming",
        description: "Minimize the remaining stone weight after repeatedly smashing stones.",
        file: "1130-last-stone-weight-ii.md",
        type: "py"
    },
    {
        slug: "114-flatten-binary-tree-to-linked-list",
        class: "leetcode",
        title: "114-flatten-binary-tree-to-linked-list",
        date: "",
        category: "tree",
        description: "Transform a binary tree into a linked list following preorder traversal order.",
        file: "114-flatten-binary-tree-to-linked-list.md",
        type: "py"
    },
    {
        slug: "1146-greatest-common-divisor-of-strings",
        class: "leetcode",
        title: "1146-greatest-common-divisor-of-strings",
        date: "",
        category: "string",
        description: "Find the largest string that can repeatedly construct two given strings.",
        file: "1146-greatest-common-divisor-of-strings.md",
        type: "py"
    },
    {
        slug: "115-distinct-subsequences",
        class: "leetcode",
        title: "115-distinct-subsequences",
        date: "",
        category: "dynamic-programming",
        description: "Count how many distinct subsequences of one string equal another string.",
        file: "115-distinct-subsequences.md",
        type: "py"
    },
    {
        slug: "117-populating-next-right-pointers-in-each-node-ii",
        class: "leetcode",
        title: "117-populating-next-right-pointers-in-each-node-ii",
        date: "",
        category: "tree",
        description: "Connect each node to its next right node in a binary tree.",
        file: "117-populating-next-right-pointers-in-each-node-ii.md",
        type: "py"
    },
    {
        slug: "1170-shortest-common-supersequence",
        class: "leetcode",
        title: "1170-shortest-common-supersequence",
        date: "",
        category: "dynamic-programming",
        description: "Construct the shortest string containing two strings as subsequences.",
        file: "1170-shortest-common-supersequence.md",
        type: "py"
    },
    {
        slug: "118-pascals-triangle",
        class: "leetcode",
        title: "118-pascals-triangle",
        date: "",
        category: "dynamic-programming",
        description: "Generate the first rows of Pascal's Triangle.",
        file: "118-pascals-triangle.md",
        type: "py"
    },
    {
        slug: "119-pascals-triangle-ii",
        class: "leetcode",
        title: "119-pascals-triangle-ii",
        date: "",
        category: "dynamic-programming",
        description: "Return a specific row of Pascal's Triangle.",
        file: "119-pascals-triangle-ii.md",
        type: "py"
    },
    {
        slug: "12-integer-to-roman",
        class: "leetcode",
        title: "12-integer-to-roman",
        date: "",
        category: "string",
        description: "Convert an integer into its Roman numeral representation.",
        file: "12-integer-to-roman.md",
        type: "py"
    },
    {
        slug: "120-triangle",
        class: "leetcode",
        title: "120-triangle",
        date: "",
        category: "dynamic-programming",
        description: "Find the minimum path sum from top to bottom of a triangle.",
        file: "120-triangle.md",
        type: "py"
    },
    {
        slug: "121-best-time-to-buy-and-sell-stock",
        class: "leetcode",
        title: "121-best-time-to-buy-and-sell-stock",
        date: "",
        category: "array",
        description: "Determine the maximum profit from a single stock transaction.",
        file: "121-best-time-to-buy-and-sell-stock.md",
        type: "py"
    },
    {
        slug: "122-best-time-to-buy-and-sell-stock-ii",
        class: "leetcode",
        title: "122-best-time-to-buy-and-sell-stock-ii",
        date: "",
        category: "greedy",
        description: "Maximize profit with unlimited stock transactions.",
        file: "122-best-time-to-buy-and-sell-stock-ii.md",
        type: "py"
    },
    {
        slug: "1220-smallest-sufficient-team",
        class: "leetcode",
        title: "1220-smallest-sufficient-team",
        date: "",
        category: "bitmask-dp",
        description: "Find the smallest team that covers all required skills.",
        file: "1220-smallest-sufficient-team.md",
        type: "py"
    },
    {
        slug: "1224-minimum-falling-path-sum-ii",
        class: "leetcode",
        title: "1224-minimum-falling-path-sum-ii",
        date: "",
        category: "dynamic-programming",
        description: "Compute the minimum falling path sum while avoiding the same column consecutively.",
        file: "1224-minimum-falling-path-sum-ii.md",
        type: "py"
    },
    {
        slug: "1228-minimum-cost-tree-from-leaf-values",
        class: "leetcode",
        title: "1228-minimum-cost-tree-from-leaf-values",
        date: "",
        category: "monotonic-stack",
        description: "Build a tree from leaf values with minimum possible non-leaf node cost.",
        file: "1228-minimum-cost-tree-from-leaf-values.md",
        type: "py"
    },
    {
        slug: "123-best-time-to-buy-and-sell-stock-iii",
        class: "leetcode",
        title: "123-best-time-to-buy-and-sell-stock-iii",
        date: "",
        category: "dynamic-programming",
        description: "Maximize stock profit using at most two transactions.",
        file: "123-best-time-to-buy-and-sell-stock-iii.md",
        type: "py"
    },
    {
        slug: "1234-number-of-paths-with-max-score",
        class: "leetcode",
        title: "1234-number-of-paths-with-max-score",
        date: "",
        category: "dynamic-programming",
        description: "Find the maximum score path and count how many such paths exist.",
        file: "1234-number-of-paths-with-max-score.md",
        type: "py"
    },
    {
        slug: "124-binary-tree-maximum-path-sum",
        class: "leetcode",
        title: "124-binary-tree-maximum-path-sum",
        date: "",
        category: "tree-dp",
        description: "Find the maximum path sum in a binary tree.",
        file: "124-binary-tree-maximum-path-sum.md",
        type: "py"
    },
    {
        slug: "1240-stone-game-ii",
        class: "leetcode",
        title: "1240-stone-game-ii",
        date: "",
        category: "dynamic-programming",
        description: "Determine the optimal score in a competitive stone-taking game.",
        file: "1240-stone-game-ii.md",
        type: "py"
    },
    {
        slug: "125-valid-palindrome",
        class: "leetcode",
        title: "125-valid-palindrome",
        date: "",
        category: "two-pointers",
        description: "Check whether a string is a palindrome after removing non-alphanumeric characters.",
        file: "125-valid-palindrome.md",
        type: "py"
    },
    {
        slug: "1250-longest-common-subsequence",
        class: "leetcode",
        title: "1250-longest-common-subsequence",
        date: "",
        category: "dynamic-programming",
        description: "Find the length of the longest common subsequence of two strings.",
        file: "1250-longest-common-subsequence.md",
        type: "py"
    },
    {
        slug: "127-word-ladder",
        class: "leetcode",
        title: "127-word-ladder",
        date: "",
        category: "bfs",
        description: "Find the shortest transformation sequence between two words.",
        file: "127-word-ladder.md",
        type: "py"
    },
    {
        slug: "128-longest-consecutive-sequence",
        class: "leetcode",
        title: "128-longest-consecutive-sequence",
        date: "",
        category: "hash-set",
        description: "Find the length of the longest sequence of consecutive integers.",
        file: "128-longest-consecutive-sequence.md",
        type: "py"
    },
    {
        slug: "1286-constrained-subsequence-sum",
        class: "leetcode",
        title: "1286-constrained-subsequence-sum",
        date: "",
        category: "monotonic-queue",
        description: "Find the maximum subsequence sum subject to a distance constraint.",
        file: "1286-constrained-subsequence-sum.md",
        type: "py"
    },
    {
        slug: "129-sum-root-to-leaf-numbers",
        class: "leetcode",
        title: "129-sum-root-to-leaf-numbers",
        date: "",
        category: "tree",
        description: "Sum all numbers formed by root-to-leaf paths in a binary tree.",
        file: "129-sum-root-to-leaf-numbers.md",
        type: "py"
    },
    {
        slug: "13-roman-to-integer",
        class: "leetcode",
        title: "13-roman-to-integer",
        date: "",
        category: "string",
        description: "Convert a Roman numeral into its integer value.",
        file: "13-roman-to-integer.md",
        type: "py"
    },
    {
        slug: "130-surrounded-regions",
        class: "leetcode",
        title: "130-surrounded-regions",
        date: "",
        category: "graph",
        description: "Capture regions completely surrounded by X characters on a board.",
        file: "130-surrounded-regions.md",
        type: "py"
    },
    {
        slug: "132-palindrome-partitioning-ii",
        class: "leetcode",
        title: "132-palindrome-partitioning-ii",
        date: "",
        category: "dynamic-programming",
        description: "Find the minimum cuts needed to partition a string into palindromes.",
        file: "132-palindrome-partitioning-ii.md",
        type: "py"
    },
    {
        slug: "133-clone-graph",
        class: "leetcode",
        title: "133-clone-graph",
        date: "",
        category: "graph",
        description: "Create a deep copy of a connected graph.",
        file: "133-clone-graph.md",
        type: "py"
    },
    {
        slug: "134-gas-station",
        class: "leetcode",
        title: "134-gas-station",
        date: "",
        category: "greedy",
        description: "Determine the starting gas station that allows completing a circular route.",
        file: "134-gas-station.md",
        type: "py"
    },
    {
        slug: "135-candy",
        class: "leetcode",
        title: "135-candy",
        date: "",
        category: "greedy",
        description: "Distribute candies to children while satisfying rating constraints with the minimum total candies.",
        file: "135-candy.md",
        type: "py"
    },
    {
        slug: "136-single-number",
        class: "leetcode",
        title: "136-single-number",
        date: "",
        category: "bit-manipulation",
        description: "Find the element that appears exactly once when all others appear twice.",
        file: "136-single-number.md",
        type: "py"
    },
    {
        slug: "137-single-number-ii",
        class: "leetcode",
        title: "137-single-number-ii",
        date: "",
        category: "bit-manipulation",
        description: "Find the element that appears once when all others appear three times.",
        file: "137-single-number-ii.md",
        type: "py"
    },
    {
        slug: "138-copy-list-with-random-pointer",
        class: "leetcode",
        title: "138-copy-list-with-random-pointer",
        date: "",
        category: "linked-list",
        description: "Create a deep copy of a linked list with random pointers.",
        file: "138-copy-list-with-random-pointer.md",
        type: "py"
    },
    {
        slug: "139-word-break",
        class: "leetcode",
        title: "139-word-break",
        date: "",
        category: "dynamic-programming",
        description: "Determine whether a string can be segmented into dictionary words.",
        file: "139-word-break.md",
        type: "py"
    },
    {
        slug: "1397-search-suggestions-system",
        class: "leetcode",
        title: "1397-search-suggestions-system",
        date: "",
        category: "trie",
        description: "Return product suggestions for each prefix of a search word.",
        file: "1397-search-suggestions-system.md",
        type: "py"
    },
    {
        slug: "1398-number-of-ways-to-stay-in-the-same-place-after-some-steps",
        class: "leetcode",
        title: "1398-number-of-ways-to-stay-in-the-same-place-after-some-steps",
        date: "",
        category: "dynamic-programming",
        description: "Count the ways to remain at the starting position after a given number of steps.",
        file: "1398-number-of-ways-to-stay-in-the-same-place-after-some-steps.md",
        type: "py"
    },
    {
        slug: "14-longest-common-prefix",
        class: "leetcode",
        title: "14-longest-common-prefix",
        date: "",
        category: "string",
        description: "Find the longest common prefix shared by a list of strings.",
        file: "14-longest-common-prefix.md",
        type: "py"
    },
    {
        slug: "1402-count-square-submatrices-with-all-ones",
        class: "leetcode",
        title: "1402-count-square-submatrices-with-all-ones",
        date: "",
        category: "dynamic-programming",
        description: "Count all square submatrices consisting entirely of ones.",
        file: "1402-count-square-submatrices-with-all-ones.md",
        type: "py"
    },
    {
        slug: "1403-palindrome-partitioning-iii",
        class: "leetcode",
        title: "1403-palindrome-partitioning-iii",
        date: "",
        category: "dynamic-programming",
        description: "Partition a string into k palindromes with the minimum number of character changes.",
        file: "1403-palindrome-partitioning-iii.md",
        type: "py"
    },
    {
        slug: "141-linked-list-cycle",
        class: "leetcode",
        title: "141-linked-list-cycle",
        date: "",
        category: "two-pointers",
        description: "Detect whether a linked list contains a cycle.",
        file: "141-linked-list-cycle.md",
        type: "py"
    },
    {
        slug: "1437-minimum-insertion-steps-to-make-a-string-palindrome",
        class: "leetcode",
        title: "1437-minimum-insertion-steps-to-make-a-string-palindrome",
        date: "",
        category: "dynamic-programming",
        description: "Find the minimum insertions required to make a string a palindrome.",
        file: "1437-minimum-insertion-steps-to-make-a-string-palindrome.md",
        type: "py"
    },
    {
        slug: "1441-minimum-flips-to-make-a-or-b-equal-to-c",
        class: "leetcode",
        title: "1441-minimum-flips-to-make-a-or-b-equal-to-c",
        date: "",
        category: "bit-manipulation",
        description: "Determine the minimum bit flips needed so that a OR b equals c.",
        file: "1441-minimum-flips-to-make-a-or-b-equal-to-c.md",
        type: "py"
    },
    {
        slug: "1443-minimum-distance-to-type-a-word-using-two-fingers",
        class: "leetcode",
        title: "1443-minimum-distance-to-type-a-word-using-two-fingers",
        date: "",
        category: "dynamic-programming",
        description: "Minimize finger movement when typing a word with two fingers.",
        file: "1443-minimum-distance-to-type-a-word-using-two-fingers.md",
        type: "py"
    },
    {
        slug: "1451-minimum-number-of-taps-to-open-to-water-a-garden",
        class: "leetcode",
        title: "1451-minimum-number-of-taps-to-open-to-water-a-garden",
        date: "",
        category: "greedy",
        description: "Find the minimum number of taps needed to water an entire garden.",
        file: "1451-minimum-number-of-taps-to-open-to-water-a-garden.md",
        type: "py"
    },
    {
        slug: "1456-find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance",
        class: "leetcode",
        title: "1456-find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance",
        date: "",
        category: "graph",
        description: "Find the city reachable from the fewest other cities within a distance threshold.",
        file: "1456-find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance.md",
        type: "py"
    },
    {
        slug: "1457-minimum-difficulty-of-a-job-schedule",
        class: "leetcode",
        title: "1457-minimum-difficulty-of-a-job-schedule",
        date: "",
        category: "dynamic-programming",
        description: "Schedule jobs across days while minimizing total difficulty.",
        file: "1457-minimum-difficulty-of-a-job-schedule.md",
        type: "py"
    },
    {
        slug: "146-lru-cache",
        class: "leetcode",
        title: "146-lru-cache",
        date: "",
        category: "design",
        description: "Implement a least recently used cache with efficient operations.",
        file: "146-lru-cache.md",
        type: "py"
    },
    {
        slug: "1466-jump-game-v",
        class: "leetcode",
        title: "1466-jump-game-v",
        date: "",
        category: "dynamic-programming",
        description: "Find the maximum number of indices reachable under constrained jumps.",
        file: "1466-jump-game-v.md",
        type: "py"
    },
    {
        slug: "1471-maximum-students-taking-exam",
        class: "leetcode",
        title: "1471-maximum-students-taking-exam",
        date: "",
        category: "bitmask-dp",
        description: "Seat the maximum number of students while preventing cheating.",
        file: "1471-maximum-students-taking-exam.md",
        type: "py"
    },
    {
        slug: "1475-maximum-sum-bst-in-binary-tree",
        class: "leetcode",
        title: "1475-maximum-sum-bst-in-binary-tree",
        date: "",
        category: "tree-dp",
        description: "Find the maximum sum of values among all BST subtrees in a binary tree.",
        file: "1475-maximum-sum-bst-in-binary-tree.md",
        type: "py"
    },
    {
        slug: "1476-count-negative-numbers-in-a-sorted-matrix",
        class: "leetcode",
        title: "1476-count-negative-numbers-in-a-sorted-matrix",
        date: "",
        category: "matrix",
        description: "Count the negative values in a row-wise and column-wise sorted matrix.",
        file: "1476-count-negative-numbers-in-a-sorted-matrix.md",
        type: "py"
    },
    {
        slug: "1477-product-of-the-last-k-numbers",
        class: "leetcode",
        title: "1477-product-of-the-last-k-numbers",
        date: "",
        category: "design",
        description: "Design a data structure that returns the product of the last k inserted numbers.",
        file: "1477-product-of-the-last-k-numbers.md",
        type: "py"
    },
    {
        slug: "148-sort-list",
        class: "leetcode",
        title: "148-sort-list",
        date: "",
        category: "linked-list",
        description: "Sort a linked list in ascending order with optimal complexity.",
        file: "148-sort-list.md",
        type: "py"
    },
    {
        slug: "149-max-points-on-a-line",
        class: "leetcode",
        title: "149-max-points-on-a-line",
        date: "",
        category: "geometry",
        description: "Find the maximum number of points that lie on the same straight line.",
        file: "149-max-points-on-a-line.md",
        type: "py"
    },
    {
        slug: "15-3sum",
        class: "leetcode",
        title: "15-3sum",
        date: "",
        category: "two-pointers",
        description: "Find all unique triplets whose sum equals zero.",
        file: "15-3sum.md",
        type: "py"
    },
    {
        slug: "150-evaluate-reverse-polish-notation",
        class: "leetcode",
        title: "150-evaluate-reverse-polish-notation",
        date: "",
        category: "stack",
        description: "Evaluate the value of an arithmetic expression in reverse Polish notation.",
        file: "150-evaluate-reverse-polish-notation.md",
        type: "py"
    },
    {
        slug: "151-reverse-words-in-a-string",
        class: "leetcode",
        title: "151-reverse-words-in-a-string",
        date: "",
        category: "string",
        description: "Reverse the order of words in a string while removing extra spaces.",
        file: "151-reverse-words-in-a-string.md",
        type: "py"
    },
    {
        slug: "152-maximum-product-subarray",
        class: "leetcode",
        title: "152-maximum-product-subarray",
        date: "",
        category: "dynamic-programming",
        description: "Find the contiguous subarray with the maximum product.",
        file: "152-maximum-product-subarray.md",
        type: "py"
    },
    {
        slug: "1522-stone-game-iii",
        class: "leetcode",
        title: "1522-stone-game-iii",
        date: "",
        category: "dynamic-programming",
        description: "Determine the winner of a stone game when both players play optimally.",
        file: "1522-stone-game-iii.md",
        type: "py"
    },
    {
        slug: "153-find-minimum-in-rotated-sorted-array",
        class: "leetcode",
        title: "153-find-minimum-in-rotated-sorted-array",
        date: "",
        category: "binary-search",
        description: "Find the minimum element in a rotated sorted array.",
        file: "153-find-minimum-in-rotated-sorted-array.md",
        type: "py"
    },
    {
        slug: "1531-number-of-ways-to-wear-different-hats-to-each-other",
        class: "leetcode",
        title: "1531-number-of-ways-to-wear-different-hats-to-each-other",
        date: "",
        category: "bitmask-dp",
        description: "Count valid assignments of hats so each person wears a unique hat.",
        file: "1531-number-of-ways-to-wear-different-hats-to-each-other.md",
        type: "py"
    },
    {
        slug: "155-min-stack",
        class: "leetcode",
        title: "155-min-stack",
        date: "",
        category: "stack",
        description: "Design a stack that supports retrieving the minimum element in constant time.",
        file: "155-min-stack.md",
        type: "py"
    },
    {
        slug: "1577-probability-of-a-two-boxes-having-the-same-number-of-distinct-balls",
        class: "leetcode",
        title: "1577-probability-of-a-two-boxes-having-the-same-number-of-distinct-balls",
        date: "",
        category: "combinatorics",
        description: "Compute the probability that two boxes contain the same number of distinct ball colors.",
        file: "1577-probability-of-a-two-boxes-having-the-same-number-of-distinct-balls.md",
        type: "py"
    },
    {
        slug: "1585-the-kth-factor-of-n",
        class: "leetcode",
        title: "1585-the-kth-factor-of-n",
        date: "",
        category: "math",
        description: "Find the kth factor of a positive integer.",
        file: "1585-the-kth-factor-of-n.md",
        type: "py"
    },
    {
        slug: "1617-stone-game-iv",
        class: "leetcode",
        title: "1617-stone-game-iv",
        date: "",
        category: "dynamic-programming",
        description: "Determine whether the first player can win a stone game with optimal play.",
        file: "1617-stone-game-iv.md",
        type: "py"
    },
    {
        slug: "162-find-peak-element",
        class: "leetcode",
        title: "162-find-peak-element",
        date: "",
        category: "binary-search",
        description: "Find an index of a peak element in an array.",
        file: "162-find-peak-element.md",
        type: "py"
    },
    {
        slug: "167-two-sum-ii-input-array-is-sorted",
        class: "leetcode",
        title: "167-two-sum-ii-input-array-is-sorted",
        date: "",
        category: "two-pointers",
        description: "Find two numbers in a sorted array whose sum equals a target value.",
        file: "167-two-sum-ii-input-array-is-sorted.md",
        type: "py"
    },
    {
        slug: "169-majority-element",
        class: "leetcode",
        title: "169-majority-element",
        date: "",
        category: "array",
        description: "Find the element that appears more than half the time in an array.",
        file: "169-majority-element.md",
        type: "py"
    },
    {
        slug: "17-letter-combinations-of-a-phone-number",
        class: "leetcode",
        title: "17-letter-combinations-of-a-phone-number",
        date: "",
        category: "backtracking",
        description: "Generate all letter combinations represented by a phone keypad number string.",
        file: "17-letter-combinations-of-a-phone-number.md",
        type: "py"
    },
    {
        slug: "172-factorial-trailing-zeroes",
        class: "leetcode",
        title: "172-factorial-trailing-zeroes",
        date: "",
        category: "math",
        description: "Count the number of trailing zeroes in a factorial.",
        file: "172-factorial-trailing-zeroes.md",
        type: "py"
    },
    {
        slug: "173-binary-search-tree-iterator",
        class: "leetcode",
        title: "173-binary-search-tree-iterator",
        date: "",
        category: "design",
        description: "Implement an iterator that traverses a binary search tree in sorted order.",
        file: "173-binary-search-tree-iterator.md",
        type: "py"
    },
    {
        slug: "188-best-time-to-buy-and-sell-stock-iv",
        class: "leetcode",
        title: "188-best-time-to-buy-and-sell-stock-iv",
        date: "",
        category: "dynamic-programming",
        description: "Maximize stock trading profit using at most k transactions.",
        file: "188-best-time-to-buy-and-sell-stock-iv.md",
        type: "py"
    },
    {
        slug: "189-rotate-array",
        class: "leetcode",
        title: "189-rotate-array",
        date: "",
        category: "array",
        description: "Rotate an array to the right by a given number of steps.",
        file: "189-rotate-array.md",
        type: "py"
    },
    {
        slug: "1894-merge-strings-alternately",
        class: "leetcode",
        title: "1894-merge-strings-alternately",
        date: "",
        category: "string",
        description: "Merge two strings by alternating characters from each.",
        file: "1894-merge-strings-alternately.md",
        type: "py"
    },
    {
        slug: "19-remove-nth-node-from-end-of-list",
        class: "leetcode",
        title: "19-remove-nth-node-from-end-of-list",
        date: "",
        category: "linked-list",
        description: "Remove the nth node from the end of a linked list.",
        file: "19-remove-nth-node-from-end-of-list.md",
        type: "py"
    },
    {
        slug: "190-reverse-bits",
        class: "leetcode",
        title: "190-reverse-bits",
        date: "",
        category: "bit-manipulation",
        description: "Reverse the bit order of a 32-bit integer.",
        file: "190-reverse-bits.md",
        type: "py"
    },
    {
        slug: "191-number-of-1-bits",
        class: "leetcode",
        title: "191-number-of-1-bits",
        date: "",
        category: "bit-manipulation",
        description: "Count the number of set bits in an integer.",
        file: "191-number-of-1-bits.md",
        type: "py"
    },
    {
        slug: "1977-minimum-interval-to-include-each-query",
        class: "leetcode",
        title: "1977-minimum-interval-to-include-each-query",
        date: "",
        category: "heap",
        description: "Find the smallest interval containing each query value.",
        file: "1977-minimum-interval-to-include-each-query.md",
        type: "py"
    },
    {
        slug: "198-house-robber",
        class: "leetcode",
        title: "198-house-robber",
        date: "",
        category: "dynamic-programming",
        description: "Maximize the amount stolen without robbing adjacent houses.",
        file: "198-house-robber.md",
        type: "py"
    },
    {
        slug: "199-binary-tree-right-side-view",
        class: "leetcode",
        title: "199-binary-tree-right-side-view",
        date: "",
        category: "tree",
        description: "Return the nodes visible when viewing a binary tree from the right side.",
        file: "199-binary-tree-right-side-view.md",
        type: "py"
    },
    {
        slug: "2-add-two-numbers",
        class: "leetcode",
        title: "2-add-two-numbers",
        date: "",
        category: "linked-list",
        description: "Add two numbers represented as linked lists.",
        file: "2-add-two-numbers.md",
        type: "py"
    },
    {
        slug: "20-valid-parentheses",
        class: "leetcode",
        title: "20-valid-parentheses",
        date: "",
        category: "stack",
        description: "Determine whether a string of brackets is properly balanced.",
        file: "20-valid-parentheses.md",
        type: "py"
    },
    {
        slug: "200-number-of-islands",
        class: "leetcode",
        title: "200-number-of-islands",
        date: "",
        category: "graph",
        description: "Count the number of islands in a grid.",
        file: "200-number-of-islands.md",
        type: "py"
    },
    {
        slug: "201-bitwise-and-of-numbers-range",
        class: "leetcode",
        title: "201-bitwise-and-of-numbers-range",
        date: "",
        category: "bit-manipulation",
        description: "Compute the bitwise AND of all numbers in a range.",
        file: "201-bitwise-and-of-numbers-range.md",
        type: "py"
    },
    {
        slug: "202-happy-number",
        class: "leetcode",
        title: "202-happy-number",
        date: "",
        category: "hash-set",
        description: "Determine whether repeatedly summing squared digits reaches one.",
        file: "202-happy-number.md",
        type: "py"
    },
    {
        slug: "205-isomorphic-strings",
        class: "leetcode",
        title: "205-isomorphic-strings",
        date: "",
        category: "hash-map",
        description: "Determine whether two strings can be transformed through a one-to-one character mapping.",
        file: "205-isomorphic-strings.md",
        type: "py"
    },
    {
        slug: "207-course-schedule",
        class: "leetcode",
        title: "207-course-schedule",
        date: "",
        category: "topological-sort",
        description: "Determine whether all courses can be completed given prerequisite relationships.",
        file: "207-course-schedule.md",
        type: "py"
    },
    {
        slug: "208-implement-trie-prefix-tree",
        class: "leetcode",
        title: "208-implement-trie-prefix-tree",
        date: "",
        category: "trie",
        description: "Implement a prefix tree supporting insertion and prefix queries.",
        file: "208-implement-trie-prefix-tree.md",
        type: "py"
    },
    {
        slug: "209-minimum-size-subarray-sum",
        class: "leetcode",
        title: "209-minimum-size-subarray-sum",
        date: "",
        category: "sliding-window",
        description: "Find the shortest subarray whose sum reaches a target value.",
        file: "209-minimum-size-subarray-sum.md",
        type: "py"
    },
    {
        slug: "2096-find-the-longest-valid-obstacle-course-at-each-position",
        class: "leetcode",
        title: "2096-find-the-longest-valid-obstacle-course-at-each-position",
        date: "",
        category: "binary-search",
        description: "Compute the longest nondecreasing obstacle course ending at each position.",
        file: "2096-find-the-longest-valid-obstacle-course-at-each-position.md",
        type: "py"
    },
    {
        slug: "21-merge-two-sorted-lists",
        class: "leetcode",
        title: "21-merge-two-sorted-lists",
        date: "",
        category: "linked-list",
        description: "Merge two sorted linked lists into one sorted list.",
        file: "21-merge-two-sorted-lists.md",
        type: "py"
    },
    {
        slug: "210-course-schedule-ii",
        class: "leetcode",
        title: "210-course-schedule-ii",
        date: "",
        category: "topological-sort",
        description: "Return a valid ordering of courses that satisfies prerequisite constraints.",
        file: "210-course-schedule-ii.md",
        type: "py"
    },
    {
        slug: "211-design-add-and-search-words-data-structure",
        class: "leetcode",
        title: "211-design-add-and-search-words-data-structure",
        date: "",
        category: "trie",
        description: "Design a word dictionary supporting wildcard searches.",
        file: "211-design-add-and-search-words-data-structure.md",
        type: "py"
    },
    {
        slug: "2114-minimum-number-of-work-sessions-to-finish-the-tasks",
        class: "leetcode",
        title: "2114-minimum-number-of-work-sessions-to-finish-the-tasks",
        date: "",
        category: "bitmask-dp",
        description: "Schedule tasks into the minimum number of work sessions.",
        file: "2114-minimum-number-of-work-sessions-to-finish-the-tasks.md",
        type: "py"
    },
    {
        slug: "2115-number-of-unique-good-subsequences",
        class: "leetcode",
        title: "2115-number-of-unique-good-subsequences",
        date: "",
        category: "dynamic-programming",
        description: "Count distinct valid subsequences in a binary string.",
        file: "2115-number-of-unique-good-subsequences.md",
        type: "py"
    },
    {
        slug: "212-word-search-ii",
        class: "leetcode",
        title: "212-word-search-ii",
        date: "",
        category: "trie",
        description: "Find all dictionary words that can be formed in a character grid.",
        file: "212-word-search-ii.md",
        type: "py"
    },
    {
        slug: "213-house-robber-ii",
        class: "leetcode",
        title: "213-house-robber-ii",
        date: "",
        category: "dynamic-programming",
        description: "Maximize robbery profit from houses arranged in a circle.",
        file: "213-house-robber-ii.md",
        type: "py"
    },
    {
        slug: "215-kth-largest-element-in-an-array",
        class: "leetcode",
        title: "215-kth-largest-element-in-an-array",
        date: "",
        category: "heap",
        description: "Find the kth largest element in an unsorted array.",
        file: "215-kth-largest-element-in-an-array.md",
        type: "py"
    },
    {
        slug: "2162-partition-array-into-two-arrays-to-minimize-sum-difference",
        class: "leetcode",
        title: "2162-partition-array-into-two-arrays-to-minimize-sum-difference",
        date: "",
        category: "meet-in-the-middle",
        description: "Partition an array into two groups with minimum difference in sums.",
        file: "2162-partition-array-into-two-arrays-to-minimize-sum-difference.md",
        type: "py"
    },
    {
        slug: "218-the-skyline-problem",
        class: "leetcode",
        title: "218-the-skyline-problem",
        date: "",
        category: "heap",
        description: "Compute the skyline formed by a collection of buildings.",
        file: "218-the-skyline-problem.md",
        type: "py"
    },
    {
        slug: "219-contains-duplicate-ii",
        class: "leetcode",
        title: "219-contains-duplicate-ii",
        date: "",
        category: "hash-map",
        description: "Determine whether duplicate values occur within a given distance.",
        file: "219-contains-duplicate-ii.md",
        type: "py"
    },
    {
        slug: "22-generate-parentheses",
        class: "leetcode",
        title: "22-generate-parentheses",
        date: "",
        category: "backtracking",
        description: "Generate all valid combinations of n pairs of parentheses.",
        file: "22-generate-parentheses.md",
        type: "py"
    },
    {
        slug: "221-maximal-square",
        class: "leetcode",
        title: "221-maximal-square",
        date: "",
        category: "dynamic-programming",
        description: "Find the area of the largest square containing only ones in a binary matrix.",
        file: "221-maximal-square.md",
        type: "py"
    },
    {
        slug: "222-count-complete-tree-nodes",
        class: "leetcode",
        title: "222-count-complete-tree-nodes",
        date: "",
        category: "tree",
        description: "Count the nodes in a complete binary tree efficiently.",
        file: "222-count-complete-tree-nodes.md",
        type: "py"
    },
    {
        slug: "224-basic-calculator",
        class: "leetcode",
        title: "224-basic-calculator",
        date: "",
        category: "stack",
        description: "Evaluate an arithmetic expression containing parentheses and operators.",
        file: "224-basic-calculator.md",
        type: "py"
    },
    {
        slug: "226-invert-binary-tree",
        class: "leetcode",
        title: "226-invert-binary-tree",
        date: "",
        category: "tree",
        description: "Invert a binary tree by swapping every node's children.",
        file: "226-invert-binary-tree.md",
        type: "py"
    },
    {
        slug: "228-summary-ranges",
        class: "leetcode",
        title: "228-summary-ranges",
        date: "",
        category: "array",
        description: "Summarize consecutive ranges in a sorted integer array.",
        file: "228-summary-ranges.md",
        type: "py"
    },
    {
        slug: "23-merge-k-sorted-lists",
        class: "leetcode",
        title: "23-merge-k-sorted-lists",
        date: "",
        category: "heap",
        description: "Merge multiple sorted linked lists into a single sorted list.",
        file: "23-merge-k-sorted-lists.md",
        type: "py"
    },
    {
        slug: "230-kth-smallest-element-in-a-bst",
        class: "leetcode",
        title: "230-kth-smallest-element-in-a-bst",
        date: "",
        category: "binary-search-tree",
        description: "Find the kth smallest value in a binary search tree.",
        file: "230-kth-smallest-element-in-a-bst.md",
        type: "py"
    },
    {
        slug: "233-number-of-digit-one",
        class: "leetcode",
        title: "233-number-of-digit-one",
        date: "",
        category: "digit-dp",
        description: "Count how many times the digit one appears from 0 to n.",
        file: "233-number-of-digit-one.md",
        type: "py"
    },
    {
        slug: "236-lowest-common-ancestor-of-a-binary-tree",
        class: "leetcode",
        title: "236-lowest-common-ancestor-of-a-binary-tree",
        date: "",
        category: "tree",
        description: "Find the lowest common ancestor of two nodes in a binary tree.",
        file: "236-lowest-common-ancestor-of-a-binary-tree.md",
        type: "py"
    },
    {
        slug: "238-product-of-array-except-self",
        class: "leetcode",
        title: "238-product-of-array-except-self",
        date: "",
        category: "array",
        description: "Compute the product of all array elements except the current one.",
        file: "238-product-of-array-except-self.md",
        type: "py"
    },
    {
        slug: "241-different-ways-to-add-parentheses",
        class: "leetcode",
        title: "241-different-ways-to-add-parentheses",
        date: "",
        category: "divide-and-conquer",
        description: "Compute all possible results from different parenthesizations of an expression.",
        file: "241-different-ways-to-add-parentheses.md",
        type: "py"
    },
    {
        slug: "242-valid-anagram",
        class: "leetcode",
        title: "242-valid-anagram",
        date: "",
        category: "hash-map",
        description: "Determine whether two strings are anagrams of each other.",
        file: "242-valid-anagram.md",
        type: "py"
    },
    {
        slug: "2432-number-of-zero-filled-subarrays",
        class: "leetcode",
        title: "2432-number-of-zero-filled-subarrays",
        date: "",
        category: "array",
        description: "Count the number of contiguous subarrays consisting entirely of zeros.",
        file: "2432-number-of-zero-filled-subarrays.md",
        type: "py"
    },
    {
        slug: "2457-count-special-integers",
        class: "leetcode",
        title: "2457-count-special-integers",
        date: "",
        category: "digit-dp",
        description: "Count positive integers with all distinct digits up to a given limit.",
        file: "2457-count-special-integers.md",
        type: "py"
    },
    {
        slug: "2487-optimal-partition-of-string",
        class: "leetcode",
        title: "2487-optimal-partition-of-string",
        date: "",
        category: "greedy",
        description: "Partition a string into the minimum number of substrings with unique characters.",
        file: "2487-optimal-partition-of-string.md",
        type: "py"
    },
    {
        slug: "25-reverse-nodes-in-k-group",
        class: "leetcode",
        title: "25-reverse-nodes-in-k-group",
        date: "",
        category: "linked-list",
        description: "Reverse linked-list nodes in groups of size k.",
        file: "25-reverse-nodes-in-k-group.md",
        type: "py"
    },
    {
        slug: "26-remove-duplicates-from-sorted-array",
        class: "leetcode",
        title: "26-remove-duplicates-from-sorted-array",
        date: "",
        category: "two-pointers",
        description: "Remove duplicates from a sorted array in place.",
        file: "26-remove-duplicates-from-sorted-array.md",
        type: "py"
    },
    {
        slug: "2627-difference-between-maximum-and-minimum-price-sum",
        class: "leetcode",
        title: "2627-difference-between-maximum-and-minimum-price-sum",
        date: "",
        category: "tree-dp",
        description: "Maximize the difference between path sums in a weighted tree.",
        file: "2627-difference-between-maximum-and-minimum-price-sum.md",
        type: "py"
    },
    {
        slug: "264-ugly-number-ii",
        class: "leetcode",
        title: "264-ugly-number-ii",
        date: "",
        category: "dynamic-programming",
        description: "Find the nth ugly number whose prime factors are limited to 2, 3, and 5.",
        file: "264-ugly-number-ii.md",
        type: "py"
    },
    {
        slug: "27-remove-element",
        class: "leetcode",
        title: "27-remove-element",
        date: "",
        category: "two-pointers",
        description: "Remove all occurrences of a value from an array in place.",
        file: "27-remove-element.md",
        type: "py"
    },
    {
        slug: "274-h-index",
        class: "leetcode",
        title: "274-h-index",
        date: "",
        category: "sorting",
        description: "Compute a researcher's h-index from citation counts.",
        file: "274-h-index.md",
        type: "py"
    },
    {
        slug: "279-perfect-squares",
        class: "leetcode",
        title: "279-perfect-squares",
        date: "",
        category: "dynamic-programming",
        description: "Find the minimum number of perfect squares that sum to a target number.",
        file: "279-perfect-squares.md",
        type: "py"
    },
    {
        slug: "28-find-the-index-of-the-first-occurrence-in-a-string",
        class: "leetcode",
        title: "28-find-the-index-of-the-first-occurrence-in-a-string",
        date: "",
        category: "string",
        description: "Find the first occurrence of one string within another.",
        file: "28-find-the-index-of-the-first-occurrence-in-a-string.md",
        type: "py"
    },
    {
        slug: "289-game-of-life",
        class: "leetcode",
        title: "289-game-of-life",
        date: "",
        category: "matrix",
        description: "Compute the next state of Conway's Game of Life in place.",
        file: "289-game-of-life.md",
        type: "py"
    },
    {
        slug: "290-word-pattern",
        class: "leetcode",
        title: "290-word-pattern",
        date: "",
        category: "hash-map",
        description: "Determine whether a string follows a specified word pattern.",
        file: "290-word-pattern.md",
        type: "py"
    },
    {
        slug: "295-find-median-from-data-stream",
        class: "leetcode",
        title: "295-find-median-from-data-stream",
        date: "",
        category: "heap",
        description: "Design a data structure that efficiently returns the median of a stream.",
        file: "295-find-median-from-data-stream.md",
        type: "py"
    },
    {
        slug: "3-longest-substring-without-repeating-characters",
        class: "leetcode",
        title: "3-longest-substring-without-repeating-characters",
        date: "",
        category: "sliding-window",
        description: "Find the length of the longest substring without repeated characters.",
        file: "3-longest-substring-without-repeating-characters.md",
        type: "py"
    },
    {
        slug: "30-substring-with-concatenation-of-all-words",
        class: "leetcode",
        title: "30-substring-with-concatenation-of-all-words",
        date: "",
        category: "sliding-window",
        description: "Find all starting indices of concatenated words in a string.",
        file: "30-substring-with-concatenation-of-all-words.md",
        type: "py"
    },
    {
        slug: "300-longest-increasing-subsequence",
        class: "leetcode",
        title: "300-longest-increasing-subsequence",
        date: "",
        category: "dynamic-programming",
        description: "Find the length of the longest strictly increasing subsequence.",
        file: "300-longest-increasing-subsequence.md",
        type: "py"
    },
    {
        slug: "307-range-sum-query-mutable",
        class: "leetcode",
        title: "307-range-sum-query-mutable",
        date: "",
        category: "segment-tree",
        description: "Support efficient range sum queries and point updates on an array.",
        file: "307-range-sum-query-mutable.md",
        type: "py"
    },
    {
        slug: "309-best-time-to-buy-and-sell-stock-with-cooldown",
        class: "leetcode",
        title: "309-best-time-to-buy-and-sell-stock-with-cooldown",
        date: "",
        category: "dynamic-programming",
        description: "Maximize stock trading profit with a cooldown period after selling.",
        file: "309-best-time-to-buy-and-sell-stock-with-cooldown.md",
        type: "py"
    },
    {
        slug: "312-burst-balloons",
        class: "leetcode",
        title: "312-burst-balloons",
        date: "",
        category: "dynamic-programming",
        description: "Maximize coins obtained by bursting balloons in an optimal order.",
        file: "312-burst-balloons.md",
        type: "py"
    },
    {
        slug: "313-super-ugly-number",
        class: "leetcode",
        title: "313-super-ugly-number",
        date: "",
        category: "dynamic-programming",
        description: "Find the nth super ugly number using a given set of prime factors.",
        file: "313-super-ugly-number.md",
        type: "py"
    },
    {
        slug: "3214-maximize-area-of-square-hole-in-grid",
        class: "leetcode",
        title: "3214-maximize-area-of-square-hole-in-grid",
        date: "",
        category: "greedy",
        description: "Determine the largest square hole that can be formed in a grid.",
        file: "3214-maximize-area-of-square-hole-in-grid.md",
        type: "py"
    },
    {
        slug: "322-coin-change",
        class: "leetcode",
        title: "322-coin-change",
        date: "",
        category: "dynamic-programming",
        description: "Find the minimum number of coins needed to reach a target amount.",
        file: "322-coin-change.md",
        type: "py"
    },
    {
        slug: "33-search-in-rotated-sorted-array",
        class: "leetcode",
        title: "33-search-in-rotated-sorted-array",
        date: "",
        category: "binary-search",
        description: "Search for a target value in a rotated sorted array.",
        file: "33-search-in-rotated-sorted-array.md",
        type: "py"
    },
    {
        slug: "337-house-robber-iii",
        class: "leetcode",
        title: "337-house-robber-iii",
        date: "",
        category: "tree-dp",
        description: "Maximize robbery amount on a binary tree without robbing adjacent nodes.",
        file: "337-house-robber-iii.md",
        type: "py"
    },
    {
        slug: "338-counting-bits",
        class: "leetcode",
        title: "338-counting-bits",
        date: "",
        category: "dynamic-programming",
        description: "Return the number of set bits for every integer from 0 to n.",
        file: "338-counting-bits.md",
        type: "py"
    },
    {
        slug: "34-find-first-and-last-position-of-element-in-sorted-array",
        class: "leetcode",
        title: "34-find-first-and-last-position-of-element-in-sorted-array",
        date: "",
        category: "binary-search",
        description: "Find the starting and ending position of a target value in a sorted array.",
        file: "34-find-first-and-last-position-of-element-in-sorted-array.md",
        type: "py"
    },
    {
        slug: "343-integer-break",
        class: "leetcode",
        title: "343-integer-break",
        date: "",
        category: "math",
        description: "Break an integer into parts to maximize their product.",
        file: "343-integer-break.md",
        type: "py"
    },
    {
        slug: "35-search-insert-position",
        class: "leetcode",
        title: "35-search-insert-position",
        date: "",
        category: "binary-search",
        description: "Find the index where a target should be inserted in a sorted array.",
        file: "35-search-insert-position.md",
        type: "py"
    },
    {
        slug: "354-russian-doll-envelopes",
        class: "leetcode",
        title: "354-russian-doll-envelopes",
        date: "",
        category: "dynamic-programming",
        description: "Find the maximum number of envelopes that can be nested.",
        file: "354-russian-doll-envelopes.md",
        type: "py"
    },
    {
        slug: "357-count-numbers-with-unique-digits",
        class: "leetcode",
        title: "357-count-numbers-with-unique-digits",
        date: "",
        category: "math",
        description: "Count numbers with all unique digits up to a given length.",
        file: "357-count-numbers-with-unique-digits.md",
        type: "py"
    },
    {
        slug: "3584-find-the-lexicographically-smallest-valid-sequence",
        class: "leetcode",
        title: "3584-find-the-lexicographically-smallest-valid-sequence",
        date: "",
        category: "greedy",
        description: "Construct the lexicographically smallest valid sequence under constraints.",
        file: "3584-find-the-lexicographically-smallest-valid-sequence.md",
        type: "py"
    },
    {
        slug: "36-valid-sudoku",
        class: "leetcode",
        title: "36-valid-sudoku",
        date: "",
        category: "hash-set",
        description: "Validate whether a Sudoku board configuration is valid.",
        file: "36-valid-sudoku.md",
        type: "py"
    },
    {
        slug: "368-largest-divisible-subset",
        class: "leetcode",
        title: "368-largest-divisible-subset",
        date: "",
        category: "dynamic-programming",
        description: "Find the largest subset where every pair is divisible.",
        file: "368-largest-divisible-subset.md",
        type: "py"
    },
    {
        slug: "373-find-k-pairs-with-smallest-sums",
        class: "leetcode",
        title: "373-find-k-pairs-with-smallest-sums",
        date: "",
        category: "heap",
        description: "Find k pairs with the smallest sums from two arrays.",
        file: "373-find-k-pairs-with-smallest-sums.md",
        type: "py"
    },
    {
        slug: "375-guess-number-higher-or-lower-ii",
        class: "leetcode",
        title: "375-guess-number-higher-or-lower-ii",
        date: "",
        category: "dynamic-programming",
        description: "Minimize cost to guarantee guessing a number correctly.",
        file: "375-guess-number-higher-or-lower-ii.md",
        type: "py"
    },
    {
        slug: "376-wiggle-subsequence",
        class: "leetcode",
        title: "376-wiggle-subsequence",
        date: "",
        category: "greedy",
        description: "Find the longest subsequence with alternating differences.",
        file: "376-wiggle-subsequence.md",
        type: "py"
    },
    {
        slug: "3763-separate-squares-i",
        class: "leetcode",
        title: "3763-separate-squares-i",
        date: "",
        category: "geometry",
        description: "Compute separation properties of squares under geometric constraints.",
        file: "3763-separate-squares-i.md",
        type: "py"
    },
    {
        slug: "377-combination-sum-iv",
        class: "leetcode",
        title: "377-combination-sum-iv",
        date: "",
        category: "dynamic-programming",
        description: "Count ordered combinations that sum to a target.",
        file: "377-combination-sum-iv.md",
        type: "py"
    },
    {
        slug: "3775-separate-squares-ii",
        class: "leetcode",
        title: "3775-separate-squares-ii",
        date: "",
        category: "geometry",
        description: "Advanced geometric partitioning of squares.",
        file: "3775-separate-squares-ii.md",
        type: "py"
    },
    {
        slug: "380-insert-delete-getrandom-o1",
        class: "leetcode",
        title: "380-insert-delete-getrandom-o1",
        date: "",
        category: "design",
        description: "Design a data structure supporting O(1) insert, delete, and random access.",
        file: "380-insert-delete-getrandom-o1.md",
        type: "py"
    },
    {
        slug: "383-ransom-note",
        class: "leetcode",
        title: "383-ransom-note",
        date: "",
        category: "hash-map",
        description: "Determine if a ransom note can be constructed from magazine letters.",
        file: "383-ransom-note.md",
        type: "py"
    },
    {
        slug: "39-combination-sum",
        class: "leetcode",
        title: "39-combination-sum",
        date: "",
        category: "backtracking",
        description: "Find all combinations that sum to a target allowing repeated elements.",
        file: "39-combination-sum.md",
        type: "py"
    },
    {
        slug: "391-perfect-rectangle",
        class: "leetcode",
        title: "391-perfect-rectangle",
        date: "",
        category: "geometry",
        description: "Determine whether rectangles perfectly cover a region without overlap.",
        file: "391-perfect-rectangle.md",
        type: "py"
    },
    {
        slug: "392-is-subsequence",
        class: "leetcode",
        title: "392-is-subsequence",
        date: "",
        category: "two-pointers",
        description: "Check if one string is a subsequence of another.",
        file: "392-is-subsequence.md",
        type: "py"
    },
    {
        slug: "396-rotate-function",
        class: "leetcode",
        title: "396-rotate-function",
        date: "",
        category: "math",
        description: "Compute maximum value of a rotation function over an array.",
        file: "396-rotate-function.md",
        type: "py"
    },
    {
        slug: "397-integer-replacement",
        class: "leetcode",
        title: "397-integer-replacement",
        date: "",
        category: "bit-manipulation",
        description: "Reduce an integer to one using minimal operations.",
        file: "397-integer-replacement.md",
        type: "py"
    },
    {
        slug: "399-evaluate-division",
        class: "leetcode",
        title: "399-evaluate-division",
        date: "",
        category: "graph",
        description: "Evaluate division queries using a weighted graph.",
        file: "399-evaluate-division.md",
        type: "py"
    },
    {
        slug: "4-median-of-two-sorted-arrays",
        class: "leetcode",
        title: "4-median-of-two-sorted-arrays",
        date: "",
        category: "binary-search",
        description: "Find the median of two sorted arrays efficiently.",
        file: "4-median-of-two-sorted-arrays.md",
        type: "py"
    },
    {
        slug: "4049-count-no-zero-pairs-that-sum-to-n",
        class: "leetcode",
        title: "4049-count-no-zero-pairs-that-sum-to-n",
        date: "",
        category: "math",
        description: "Count pairs summing to n under digit constraints.",
        file: "4049-count-no-zero-pairs-that-sum-to-n.md",
        type: "py"
    },
    {
        slug: "413-arithmetic-slices",
        class: "leetcode",
        title: "413-arithmetic-slices",
        date: "",
        category: "dynamic-programming",
        description: "Count arithmetic subarrays with constant difference.",
        file: "413-arithmetic-slices.md",
        type: "py"
    },
    {
        slug: "416-partition-equal-subset-sum",
        class: "leetcode",
        title: "416-partition-equal-subset-sum",
        date: "",
        category: "dynamic-programming",
        description: "Determine if an array can be partitioned into two equal-sum subsets.",
        file: "416-partition-equal-subset-sum.md",
        type: "py"
    },
    {
        slug: "42-trapping-rain-water",
        class: "leetcode",
        title: "42-trapping-rain-water",
        date: "",
        category: "two-pointers",
        description: "Compute how much rainwater can be trapped between bars.",
        file: "42-trapping-rain-water.md",
        type: "py"
    },
    {
        slug: "433-minimum-genetic-mutation",
        class: "leetcode",
        title: "433-minimum-genetic-mutation",
        date: "",
        category: "graph",
        description: "Find the minimum mutations needed to transform one gene into another.",
        file: "433-minimum-genetic-mutation.md",
        type: "py"
    },
    {
        slug: "435-non-overlapping-intervals",
        class: "leetcode",
        title: "435-non-overlapping-intervals",
        date: "",
        category: "greedy",
        description: "Remove minimum intervals to eliminate overlaps.",
        file: "435-non-overlapping-intervals.md",
        type: "py"
    },
    {
        slug: "44-wildcard-matching",
        class: "leetcode",
        title: "44-wildcard-matching",
        date: "",
        category: "dynamic-programming",
        description: "Match a string with wildcard patterns.",
        file: "44-wildcard-matching.md",
        type: "py"
    },
    {
        slug: "446-arithmetic-slices-ii-subsequence",
        class: "leetcode",
        title: "446-arithmetic-slices-ii-subsequence",
        date: "",
        category: "dynamic-programming",
        description: "Count arithmetic subsequences in an array.",
        file: "446-arithmetic-slices-ii-subsequence.md",
        type: "py"
    },
    {
        slug: "45-jump-game-ii",
        class: "leetcode",
        title: "45-jump-game-ii",
        date: "",
        category: "greedy",
        description: "Find minimum jumps to reach the end of an array.",
        file: "45-jump-game-ii.md",
        type: "py"
    },
    {
        slug: "452-minimum-number-of-arrows-to-burst-balloons",
        class: "leetcode",
        title: "452-minimum-number-of-arrows-to-burst-balloons",
        date: "",
        category: "greedy",
        description: "Find minimum arrows needed to burst all balloons represented as intervals.",
        file: "452-minimum-number-of-arrows-to-burst-balloons.md",
        type: "py"
    },
    {
        slug: "46-permutations",
        class: "leetcode",
        title: "46-permutations",
        date: "",
        category: "backtracking",
        description: "Generate all permutations of a list of numbers.",
        file: "46-permutations.md",
        type: "py"
    },
    {
        slug: "464-can-i-win",
        class: "leetcode",
        title: "464-can-i-win",
        date: "",
        category: "game-theory",
        description: "Determine if the first player can win a number picking game.",
        file: "464-can-i-win.md",
        type: "py"
    },
    {
        slug: "467-unique-substrings-in-wraparound-string",
        class: "leetcode",
        title: "467-unique-substrings-in-wraparound-string",
        date: "",
        category: "string",
        description: "Count unique substrings in a wraparound alphabet string.",
        file: "467-unique-substrings-in-wraparound-string.md",
        type: "py"
    },
    {
        slug: "473-matchsticks-to-square",
        class: "leetcode",
        title: "473-matchsticks-to-square",
        date: "",
        category: "backtracking",
        description: "Determine whether matchsticks can form a square.",
        file: "473-matchsticks-to-square.md",
        type: "py"
    },
    {
        slug: "474-ones-and-zeroes",
        class: "leetcode",
        title: "474-ones-and-zeroes",
        date: "",
        category: "dynamic-programming",
        description: "Find the maximum number of strings that can be formed with limited zeros and ones.",
        file: "474-ones-and-zeroes.md",
        type: "py"
    },
    {
        slug: "48-rotate-image",
        class: "leetcode",
        title: "48-rotate-image",
        date: "",
        category: "matrix",
        description: "Rotate an n x n matrix by 90 degrees clockwise in place.",
        file: "48-rotate-image.md",
        type: "py"
    },
    {
        slug: "486-predict-the-winner",
        class: "leetcode",
        title: "486-predict-the-winner",
        date: "",
        category: "game-theory",
        description: "Determine whether the first player can win a pick-from-ends game.",
        file: "486-predict-the-winner.md",
        type: "py"
    },
    {
        slug: "49-group-anagrams",
        class: "leetcode",
        title: "49-group-anagrams",
        date: "",
        category: "hash-map",
        description: "Group strings that are anagrams of each other.",
        file: "49-group-anagrams.md",
        type: "py"
    },
    {
        slug: "494-target-sum",
        class: "leetcode",
        title: "494-target-sum",
        date: "",
        category: "dynamic-programming",
        description: "Count ways to assign + and - signs to reach a target sum.",
        file: "494-target-sum.md",
        type: "py"
    },
    {
        slug: "5-longest-palindromic-substring",
        class: "leetcode",
        title: "5-longest-palindromic-substring",
        date: "",
        category: "string",
        description: "Find the longest palindromic substring in a string.",
        file: "5-longest-palindromic-substring.md",
        type: "py"
    },
    {
        slug: "50-powx-n",
        class: "leetcode",
        title: "50-powx-n",
        date: "",
        category: "math",
        description: "Compute x raised to the power n efficiently.",
        file: "50-powx-n.md",
        type: "py"
    },
    {
        slug: "502-ipo",
        class: "leetcode",
        title: "502-ipo",
        date: "",
        category: "greedy",
        description: "Maximize capital by selecting at most k projects.",
        file: "502-ipo.md",
        type: "py"
    },
    {
        slug: "516-longest-palindromic-subsequence",
        class: "leetcode",
        title: "516-longest-palindromic-subsequence",
        date: "",
        category: "dynamic-programming",
        description: "Find the longest palindromic subsequence in a string.",
        file: "516-longest-palindromic-subsequence.md",
        type: "py"
    },
    {
        slug: "518-coin-change-ii",
        class: "leetcode",
        title: "518-coin-change-ii",
        date: "",
        category: "dynamic-programming",
        description: "Count combinations of coins that sum to a target amount.",
        file: "518-coin-change-ii.md",
        type: "py"
    },
    {
        slug: "52-n-queens-ii",
        class: "leetcode",
        title: "52-n-queens-ii",
        date: "",
        category: "backtracking",
        description: "Count the number of valid solutions to the N-Queens problem.",
        file: "52-n-queens-ii.md",
        type: "py"
    },
    {
        slug: "526-beautiful-arrangement",
        class: "leetcode",
        title: "526-beautiful-arrangement",
        date: "",
        category: "backtracking",
        description: "Count arrangements satisfying divisibility constraints.",
        file: "526-beautiful-arrangement.md",
        type: "py"
    },
    {
        slug: "53-maximum-subarray",
        class: "leetcode",
        title: "53-maximum-subarray",
        date: "",
        category: "dynamic-programming",
        description: "Find the maximum sum of a contiguous subarray.",
        file: "53-maximum-subarray.md",
        type: "py"
    },
    {
        slug: "530-minimum-absolute-difference-in-bst",
        class: "leetcode",
        title: "530-minimum-absolute-difference-in-bst",
        date: "",
        category: "binary-search-tree",
        description: "Find the minimum difference between values in a BST.",
        file: "530-minimum-absolute-difference-in-bst.md",
        type: "py"
    },
    {
        slug: "54-spiral-matrix",
        class: "leetcode",
        title: "54-spiral-matrix",
        date: "",
        category: "matrix",
        description: "Return all elements of a matrix in spiral order.",
        file: "54-spiral-matrix.md",
        type: "py"
    },
    {
        slug: "542-01-matrix",
        class: "leetcode",
        title: "542-01-matrix",
        date: "",
        category: "graph",
        description: "Compute distance to nearest zero in a binary matrix.",
        file: "542-01-matrix.md",
        type: "py"
    },
    {
        slug: "543-diameter-of-binary-tree",
        class: "leetcode",
        title: "543-diameter-of-binary-tree",
        date: "",
        category: "tree",
        description: "Find the longest path between any two nodes in a binary tree.",
        file: "543-diameter-of-binary-tree.md",
        type: "py"
    },
    {
        slug: "55-jump-game",
        class: "leetcode",
        title: "55-jump-game",
        date: "",
        category: "greedy",
        description: "Determine if you can reach the end of an array given jump constraints.",
        file: "55-jump-game.md",
        type: "py"
    },
    {
        slug: "553-optimal-division",
        class: "leetcode",
        title: "553-optimal-division",
        date: "",
        category: "math",
        description: "Find optimal placement of division operators to maximize result.",
        file: "553-optimal-division.md",
        type: "py"
    },
    {
        slug: "56-merge-intervals",
        class: "leetcode",
        title: "56-merge-intervals",
        date: "",
        category: "intervals",
        description: "Merge overlapping intervals in a list.",
        file: "56-merge-intervals.md",
        type: "py"
    },
    {
        slug: "57-insert-interval",
        class: "leetcode",
        title: "57-insert-interval",
        date: "",
        category: "intervals",
        description: "Insert a new interval into a list of sorted intervals.",
        file: "57-insert-interval.md",
        type: "py"
    },
    {
        slug: "576-out-of-boundary-paths",
        class: "leetcode",
        title: "576-out-of-boundary-paths",
        date: "",
        category: "dynamic-programming",
        description: "Count paths that move a ball out of a grid boundary.",
        file: "576-out-of-boundary-paths.md",
        type: "py"
    },
    {
        slug: "58-length-of-last-word",
        class: "leetcode",
        title: "58-length-of-last-word",
        date: "",
        category: "string",
        description: "Return the length of the last word in a string.",
        file: "58-length-of-last-word.md",
        type: "py"
    },
    {
        slug: "583-delete-operation-for-two-strings",
        class: "leetcode",
        title: "583-delete-operation-for-two-strings",
        date: "",
        category: "dynamic-programming",
        description: "Find minimum deletions to make two strings equal.",
        file: "583-delete-operation-for-two-strings.md",
        type: "py"
    },
    {
        slug: "6-zigzag-conversion",
        class: "leetcode",
        title: "6-zigzag-conversion",
        date: "",
        category: "string",
        description: "Convert a string into a zigzag pattern and read row-wise.",
        file: "6-zigzag-conversion.md",
        type: "py"
    },
    {
        slug: "61-rotate-list",
        class: "leetcode",
        title: "61-rotate-list",
        date: "",
        category: "linked-list",
        description: "Rotate a linked list to the right by k places.",
        file: "61-rotate-list.md",
        type: "py"
    },
    {
        slug: "62-unique-paths",
        class: "leetcode",
        title: "62-unique-paths",
        date: "",
        category: "dynamic-programming",
        description: "Count unique paths in a grid from top-left to bottom-right.",
        file: "62-unique-paths.md",
        type: "py"
    },
    {
        slug: "63-unique-paths-ii",
        class: "leetcode",
        title: "63-unique-paths-ii",
        date: "",
        category: "dynamic-programming",
        description: "Count unique paths in a grid with obstacles.",
        file: "63-unique-paths-ii.md",
        type: "py"
    },
    {
        slug: "637-average-of-levels-in-binary-tree",
        class: "leetcode",
        title: "637-average-of-levels-in-binary-tree",
        date: "",
        category: "tree",
        description: "Compute average value of nodes at each tree level.",
        file: "637-average-of-levels-in-binary-tree.md",
        type: "py"
    },
    {
        slug: "64-minimum-path-sum",
        class: "leetcode",
        title: "64-minimum-path-sum",
        date: "",
        category: "dynamic-programming",
        description: "Find path with minimum sum in a grid.",
        file: "64-minimum-path-sum.md",
        type: "py"
    },
    {
        slug: "646-maximum-length-of-pair-chain",
        class: "leetcode",
        title: "646-maximum-length-of-pair-chain",
        date: "",
        category: "greedy",
        description: "Find the longest chain of pairs with increasing order.",
        file: "646-maximum-length-of-pair-chain.md",
        type: "py"
    },
    {
        slug: "647-palindromic-substrings",
        class: "leetcode",
        title: "647-palindromic-substrings",
        date: "",
        category: "string",
        description: "Count all palindromic substrings in a string.",
        file: "647-palindromic-substrings.md",
        type: "py"
    },
    {
        slug: "650-2-keys-keyboard",
        class: "leetcode",
        title: "650-2-keys-keyboard",
        date: "",
        category: "math",
        description: "Find minimum steps to reach n characters using copy-paste operations.",
        file: "650-2-keys-keyboard.md",
        type: "py"
    },
    {
        slug: "66-plus-one",
        class: "leetcode",
        title: "66-plus-one",
        date: "",
        category: "math",
        description: "Add one to a number represented as an array.",
        file: "66-plus-one.md",
        type: "py"
    },
    {
        slug: "67-add-binary",
        class: "leetcode",
        title: "67-add-binary",
        date: "",
        category: "bit-manipulation",
        description: "Add two binary strings.",
        file: "67-add-binary.md",
        type: "py"
    },
    {
        slug: "673-number-of-longest-increasing-subsequence",
        class: "leetcode",
        title: "673-number-of-longest-increasing-subsequence",
        date: "",
        category: "dynamic-programming",
        description: "Count the number of longest increasing subsequences.",
        file: "673-number-of-longest-increasing-subsequence.md",
        type: "py"
    },
    {
        slug: "68-text-justification",
        class: "leetcode",
        title: "68-text-justification",
        date: "",
        category: "string",
        description: "Fully justify text to fit a given width.",
        file: "68-text-justification.md",
        type: "py"
    },
    {
        slug: "688-knight-probability-in-chessboard",
        class: "leetcode",
        title: "688-knight-probability-in-chessboard",
        date: "",
        category: "dynamic-programming",
        description: "Compute probability a knight remains on a chessboard after moves.",
        file: "688-knight-probability-in-chessboard.md",
        type: "py"
    },
    {
        slug: "69-sqrtx",
        class: "leetcode",
        title: "69-sqrtx",
        date: "",
        category: "binary-search",
        description: "Compute the integer square root of a number.",
        file: "69-sqrtx.md",
        type: "py"
    },
    {
        slug: "698-partition-to-k-equal-sum-subsets",
        class: "leetcode",
        title: "698-partition-to-k-equal-sum-subsets",
        date: "",
        category: "backtracking",
        description: "Determine if array can be partitioned into k subsets with equal sum.",
        file: "698-partition-to-k-equal-sum-subsets.md",
        type: "py"
    },
    {
        slug: "70-climbing-stairs",
        class: "leetcode",
        title: "70-climbing-stairs",
        date: "",
        category: "dynamic-programming",
        description: "Count ways to climb stairs using 1 or 2 steps.",
        file: "70-climbing-stairs.md",
        type: "py"
    },
    {
        slug: "71-simplify-path",
        class: "leetcode",
        title: "71-simplify-path",
        date: "",
        category: "stack",
        description: "Simplify a Unix-style file path.",
        file: "71-simplify-path.md",
        type: "py"
    },
    {
        slug: "712-minimum-ascii-delete-sum-for-two-strings",
        class: "leetcode",
        title: "712-minimum-ascii-delete-sum-for-two-strings",
        date: "",
        category: "dynamic-programming",
        description: "Minimize ASCII delete sum to make two strings equal.",
        file: "712-minimum-ascii-delete-sum-for-two-strings.md",
        type: "py"
    },
    {
        slug: "714-best-time-to-buy-and-sell-stock-with-transaction-fee",
        class: "leetcode",
        title: "714-best-time-to-buy-and-sell-stock-with-transaction-fee",
        date: "",
        category: "dynamic-programming",
        description: "Maximize stock profit with transaction fees.",
        file: "714-best-time-to-buy-and-sell-stock-with-transaction-fee.md",
        type: "py"
    },
    {
        slug: "718-maximum-length-of-repeated-subarray",
        class: "leetcode",
        title: "718-maximum-length-of-repeated-subarray",
        date: "",
        category: "dynamic-programming",
        description: "Find the longest common subarray between two arrays.",
        file: "718-maximum-length-of-repeated-subarray.md",
        type: "py"
    },
    {
        slug: "72-edit-distance",
        class: "leetcode",
        title: "72-edit-distance",
        date: "",
        category: "dynamic-programming",
        description: "Compute the minimum number of operations required to convert one string into another.",
        file: "72-edit-distance.md",
        type: "py"
    },
    {
        slug: "73-set-matrix-zeroes",
        class: "leetcode",
        title: "73-set-matrix-zeroes",
        date: "",
        category: "matrix",
        description: "Set entire rows and columns to zero if an element is zero.",
        file: "73-set-matrix-zeroes.md",
        type: "py"
    },
    {
        slug: "74-search-a-2d-matrix",
        class: "leetcode",
        title: "74-search-a-2d-matrix",
        date: "",
        category: "binary-search",
        description: "Search for a target value in a sorted 2D matrix.",
        file: "74-search-a-2d-matrix.md",
        type: "py"
    },
    {
        slug: "740-delete-and-earn",
        class: "leetcode",
        title: "740-delete-and-earn",
        date: "",
        category: "dynamic-programming",
        description: "Maximize points by deleting numbers and their adjacent values.",
        file: "740-delete-and-earn.md",
        type: "py"
    },
    {
        slug: "747-min-cost-climbing-stairs",
        class: "leetcode",
        title: "747-min-cost-climbing-stairs",
        date: "",
        category: "dynamic-programming",
        description: "Find minimum cost to reach the top of stairs.",
        file: "747-min-cost-climbing-stairs.md",
        type: "py"
    },
    {
        slug: "76-minimum-window-substring",
        class: "leetcode",
        title: "76-minimum-window-substring",
        date: "",
        category: "sliding-window",
        description: "Find the smallest substring containing all characters of another string.",
        file: "76-minimum-window-substring.md",
        type: "py"
    },
    {
        slug: "769-largest-plus-sign",
        class: "leetcode",
        title: "769-largest-plus-sign",
        date: "",
        category: "dynamic-programming",
        description: "Find the largest plus sign in a grid with mines.",
        file: "769-largest-plus-sign.md",
        type: "py"
    },
    {
        slug: "77-combinations",
        class: "leetcode",
        title: "77-combinations",
        date: "",
        category: "backtracking",
        description: "Generate all combinations of k numbers out of 1 to n.",
        file: "77-combinations.md",
        type: "py"
    },
    {
        slug: "772-construct-quad-tree",
        class: "leetcode",
        title: "772-construct-quad-tree",
        date: "",
        category: "divide-and-conquer",
        description: "Construct a quad tree from a binary grid.",
        file: "772-construct-quad-tree.md",
        type: "py"
    },
    {
        slug: "79-word-search",
        class: "leetcode",
        title: "79-word-search",
        date: "",
        category: "backtracking",
        description: "Determine if a word exists in a grid by adjacent cells.",
        file: "79-word-search.md",
        type: "py"
    },
    {
        slug: "80-remove-duplicates-from-sorted-array-ii",
        class: "leetcode",
        title: "80-remove-duplicates-from-sorted-array-ii",
        date: "",
        category: "two-pointers",
        description: "Remove duplicates from sorted array allowing at most two occurrences.",
        file: "80-remove-duplicates-from-sorted-array-ii.md",
        type: "py"
    },
    {
        slug: "803-cheapest-flights-within-k-stops",
        class: "leetcode",
        title: "803-cheapest-flights-within-k-stops",
        date: "",
        category: "graph",
        description: "Find cheapest flight with at most K stops.",
        file: "803-cheapest-flights-within-k-stops.md",
        type: "py"
    },
    {
        slug: "804-rotated-digits",
        class: "leetcode",
        title: "804-rotated-digits",
        date: "",
        category: "math",
        description: "Count numbers that remain valid after rotation.",
        file: "804-rotated-digits.md",
        type: "py"
    },
    {
        slug: "806-domino-and-tromino-tiling",
        class: "leetcode",
        title: "806-domino-and-tromino-tiling",
        date: "",
        category: "dynamic-programming",
        description: "Count ways to tile a board using dominoes and trominoes.",
        file: "806-domino-and-tromino-tiling.md",
        type: "py"
    },
    {
        slug: "808-number-of-matching-subsequences",
        class: "leetcode",
        title: "808-number-of-matching-subsequences",
        date: "",
        category: "string",
        description: "Count how many words are subsequences of a string.",
        file: "808-number-of-matching-subsequences.md",
        type: "py"
    },
    {
        slug: "815-champagne-tower",
        class: "leetcode",
        title: "815-champagne-tower",
        date: "",
        category: "simulation",
        description: "Simulate champagne overflow in a pyramid structure.",
        file: "815-champagne-tower.md",
        type: "py"
    },
    {
        slug: "82-remove-duplicates-from-sorted-list-ii",
        class: "leetcode",
        title: "82-remove-duplicates-from-sorted-list-ii",
        date: "",
        category: "linked-list",
        description: "Remove all nodes that have duplicates in a sorted linked list.",
        file: "82-remove-duplicates-from-sorted-list-ii.md",
        type: "py"
    },
    {
        slug: "826-soup-servings",
        class: "leetcode",
        title: "826-soup-servings",
        date: "",
        category: "probability",
        description: "Compute probability of soup serving depletion scenarios.",
        file: "826-soup-servings.md",
        type: "py"
    },
    {
        slug: "831-largest-sum-of-averages",
        class: "leetcode",
        title: "831-largest-sum-of-averages",
        date: "",
        category: "dynamic-programming",
        description: "Partition array to maximize sum of averages.",
        file: "831-largest-sum-of-averages.md",
        type: "py"
    },
    {
        slug: "843-binary-trees-with-factors",
        class: "leetcode",
        title: "843-binary-trees-with-factors",
        date: "",
        category: "dynamic-programming",
        description: "Count binary trees where nodes are products of children.",
        file: "843-binary-trees-with-factors.md",
        type: "py"
    },
    {
        slug: "85-maximal-rectangle",
        class: "leetcode",
        title: "85-maximal-rectangle",
        date: "",
        category: "stack",
        description: "Find the largest rectangle containing only 1s in a matrix.",
        file: "85-maximal-rectangle.md",
        type: "py"
    },
    {
        slug: "86-partition-list",
        class: "leetcode",
        title: "86-partition-list",
        date: "",
        category: "linked-list",
        description: "Partition a linked list around a value.",
        file: "86-partition-list.md",
        type: "py"
    },
    {
        slug: "867-new-21-game",
        class: "leetcode",
        title: "867-new-21-game",
        date: "",
        category: "probability",
        description: "Compute probability of winning a simplified card game.",
        file: "867-new-21-game.md",
        type: "py"
    },
    {
        slug: "868-push-dominoes",
        class: "leetcode",
        title: "868-push-dominoes",
        date: "",
        category: "simulation",
        description: "Simulate falling dominoes after pushes.",
        file: "868-push-dominoes.md",
        type: "py"
    },
    {
        slug: "875-longest-mountain-in-array",
        class: "leetcode",
        title: "875-longest-mountain-in-array",
        date: "",
        category: "two-pointers",
        description: "Find longest mountain subarray.",
        file: "875-longest-mountain-in-array.md",
        type: "py"
    },
    {
        slug: "877-shortest-path-visiting-all-nodes",
        class: "leetcode",
        title: "877-shortest-path-visiting-all-nodes",
        date: "",
        category: "graph",
        description: "Find shortest path that visits all nodes.",
        file: "877-shortest-path-visiting-all-nodes.md",
        type: "py"
    },
    {
        slug: "88-merge-sorted-array",
        class: "leetcode",
        title: "88-merge-sorted-array",
        date: "",
        category: "two-pointers",
        description: "Merge two sorted arrays in place.",
        file: "88-merge-sorted-array.md",
        type: "py"
    },
    {
        slug: "880-rectangle-area-ii",
        class: "leetcode",
        title: "880-rectangle-area-ii",
        date: "",
        category: "geometry",
        description: "Compute union area of multiple rectangles.",
        file: "880-rectangle-area-ii.md",
        type: "py"
    },
    {
        slug: "9-palindrome-number",
        class: "leetcode",
        title: "9-palindrome-number",
        date: "",
        category: "math",
        description: "Check if an integer is a palindrome.",
        file: "9-palindrome-number.md",
        type: "py"
    },
    {
        slug: "905-length-of-longest-fibonacci-subsequence",
        class: "leetcode",
        title: "905-length-of-longest-fibonacci-subsequence",
        date: "",
        category: "dynamic-programming",
        description: "Find longest Fibonacci-like subsequence.",
        file: "905-length-of-longest-fibonacci-subsequence.md",
        type: "py"
    },
    {
        slug: "909-stone-game",
        class: "leetcode",
        title: "909-stone-game",
        date: "",
        category: "game-theory",
        description: "Determine winner of optimal stone picking game.",
        file: "909-stone-game.md",
        type: "py"
    },
    {
        slug: "91-decode-ways",
        class: "leetcode",
        title: "91-decode-ways",
        date: "",
        category: "dynamic-programming",
        description: "Count ways to decode a digit string into letters.",
        file: "91-decode-ways.md",
        type: "py"
    },
    {
        slug: "92-reverse-linked-list-ii",
        class: "leetcode",
        title: "92-reverse-linked-list-ii",
        date: "",
        category: "linked-list",
        description: "Reverse a portion of a linked list.",
        file: "92-reverse-linked-list-ii.md",
        type: "py"
    },
    {
        slug: "938-numbers-at-most-n-given-digit-set",
        class: "leetcode",
        title: "938-numbers-at-most-n-given-digit-set",
        date: "",
        category: "math",
        description: "Count numbers up to n using a given digit set.",
        file: "938-numbers-at-most-n-given-digit-set.md",
        type: "py"
    },
    {
        slug: "945-snakes-and-ladders",
        class: "leetcode",
        title: "945-snakes-and-ladders",
        date: "",
        category: "graph",
        description: "Find minimum moves in a snakes and ladders board.",
        file: "945-snakes-and-ladders.md",
        type: "py"
    },
    {
        slug: "95-unique-binary-search-trees-ii",
        class: "leetcode",
        title: "95-unique-binary-search-trees-ii",
        date: "",
        category: "dynamic-programming",
        description: "Generate all unique BST structures for n nodes.",
        file: "95-unique-binary-search-trees-ii.md",
        type: "py"
    },
    {
        slug: "954-maximum-sum-circular-subarray",
        class: "leetcode",
        title: "954-maximum-sum-circular-subarray",
        date: "",
        category: "dynamic-programming",
        description: "Find maximum subarray sum in a circular array.",
        file: "954-maximum-sum-circular-subarray.md",
        type: "py"
    },
    {
        slug: "96-unique-binary-search-trees",
        class: "leetcode",
        title: "96-unique-binary-search-trees",
        date: "",
        category: "dynamic-programming",
        description: "Count number of unique BSTs.",
        file: "96-unique-binary-search-trees.md",
        type: "py"
    },
    {
        slug: "967-minimum-falling-path-sum",
        class: "leetcode",
        title: "967-minimum-falling-path-sum",
        date: "",
        category: "dynamic-programming",
        description: "Find minimum falling path sum in a matrix.",
        file: "967-minimum-falling-path-sum.md",
        type: "py"
    },
    {
        slug: "97-interleaving-string",
        class: "leetcode",
        title: "97-interleaving-string",
        date: "",
        category: "dynamic-programming",
        description: "Check if a string is an interleaving of two others.",
        file: "97-interleaving-string.md",
        type: "py"
    },
    {
        slug: "977-distinct-subsequences-ii",
        class: "leetcode",
        title: "977-distinct-subsequences-ii",
        date: "",
        category: "dynamic-programming",
        description: "Count distinct subsequences of a string.",
        file: "977-distinct-subsequences-ii.md",
        type: "py"
    },
    {
        slug: "98-validate-binary-search-tree",
        class: "leetcode",
        title: "98-validate-binary-search-tree",
        date: "",
        category: "binary-tree",
        description: "Validate whether a binary tree is a BST.",
        file: "98-validate-binary-search-tree.md",
        type: "py"
    },
    {
        slug: "980-find-the-shortest-superstring",
        class: "leetcode",
        title: "980-find-the-shortest-superstring",
        date: "",
        category: "dynamic-programming",
        description: "Find the shortest superstring containing all strings.",
        file: "980-find-the-shortest-superstring.md",
        type: "py"
    },
    {
        slug: "993-tallest-billboard",
        class: "leetcode",
        title: "993-tallest-billboard",
        date: "",
        category: "dynamic-programming",
        description: "Build tallest billboard with equal support constraints.",
        file: "993-tallest-billboard.md",
        type: "py"
    }
]
