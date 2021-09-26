module FfiExamples

function run()
    a = 0
    for i in 0:1_000_000
        a += i % 2 - 0.5
    end
    
    println(a)
    "Julia"
end

end # module
