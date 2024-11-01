function IsPrime(num)
    if num <= 1 then
        return false
    elseif num <= 3 then
        return true
    elseif num % 2 == 0 or num % 3 == 0 then
        return false
    end
    local i = 5
    while i * i <= num do
        if num % i == 0 or num % (i + 2) == 0 then
            return false
        end
        i = i + 6
    end
    return true
end


function NthPrime(n)
    local count = 0
    local num = 2
    while count < n do
        if IsPrime(num) then
            count = count + 1
        end
        if count == n then
            return num
        end
        num = num + 1
    end
end

function GetLeastValue(a)
    local i, r, n = 1, 0, 0
    while r < tonumber(a) do
        n = NthPrime(i)
        r = (((n - 1) ^ i) + ((n + 1) ^ i)) % (n * n)
        i = i + 2
    end
    return n
end

local val = GetLeastValue(arg[1])
print(val)