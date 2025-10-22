class Solution:
    def countOfAtoms(self, formula):
        import re
        stack = [collections.Counter()]
        i = 0
        while i < len(formula):
            if formula[i] == '(':
                stack.append(collections.Counter()); i += 1
            elif formula[i] == ')':
                i += 1
                j = i
                while j < len(formula) and formula[j].isdigit():
                    j += 1
                mult = int(formula[i:j] or 1)
                top = stack.pop()
                for k in top:
                    stack[-1][k] += top[k]*mult
                i = j
            else:
                j = i + 1
                while j < len(formula) and formula[j].islower():
                    j += 1
                atom = formula[i:j]
                i = j
                j = i
                while j < len(formula) and formula[j].isdigit():
                    j += 1
                count = int(formula[i:j] or 1)
                stack[-1][atom] += count
                i = j
        return ''.join(k + (str(v) if v > 1 else '') for k, v in sorted(stack[-1].items()))

