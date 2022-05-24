From mathcomp Require Import all_ssreflect.

Fixpoint fibonacci (x: nat) := match x with
	| 0 => 1
	| (S x') => match x' with
		| 0 => 1
		| (S x'') => (fibonacci x') + (fibonacci x'')
		end
	end.

Definition print (x: nat) := 
	Check x.

print 101.
