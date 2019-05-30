
from generator import generate
from testcase import TestCase

x = TestCase("coriknl")
x.jobname = "exp1"
x.jana_legacy_mode = 0
x.comment = "This is a first attempt"

y = TestCase("farm18")
y.jobname = "exp2"
y.platform = "farm18"
y.jana_legacy_mode = 33
y.comment = "This is a second attempt"

generate(x)
generate(y)

