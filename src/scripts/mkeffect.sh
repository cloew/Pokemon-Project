
effect=$1"_delegate.py"
test=$1"_test.py"

effect_dir="$poke_src/Battle/Attack/EffectDelegates"

cp $poke_src/templates/effect_delegate_template.py $effect_dir/$effect
cp $poke_src/Test/testcase_template.py $effect_dir/Test/$test