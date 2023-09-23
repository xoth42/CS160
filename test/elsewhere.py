def found_elsewhere(lint,target,index):
    for i in range(len(lint)):
        if i != index:
            if lint[i] == target:
                return True
    return False

if __name__=="__main__":
    print(found_elsewhere([1,2,3],1,1))
