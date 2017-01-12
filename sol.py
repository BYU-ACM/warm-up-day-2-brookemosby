def Binary_Search(arr, to_find):

  
    def recurse (arr,cur_pos, to_find):
        if arr[cur_pos]==to_find:
            return cur_pos
        elif arr[cur_pos]<to_find:
            return recurse(arr[len(arr)/2:],len(arr)/4,to_find) +len(arr)/2
        else:
            return recurse(arr[:len(arr)/2],len(arr)/4,to_find)
    return recurse (arr,len(arr)/2,to_find)
    
    
    
    

def Bisection(func, left_side, right_side, tol=1e-5):
  """A direct implementation of Newton's Method
     (For sanity assume that func and func_prime define there own division correctly,
     that is, don't cast anything to a float)
     params: func (a function)
             left_side (a value for the function to take on, it should have opposite sign from `right_side`)
             right_side (a value for the function to take on, it should have opposite sign from `left_side`)
             tol (a value for which the function should return once a value at least that distance from zero is found)
     returns: root (float), x, s.t. abs(func(x))<tol
              None(none-type) if func(left_side), func(right_side) < 0 or func(left_side), func(right_side) > 0
  """
  pass
