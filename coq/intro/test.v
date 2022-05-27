From Coq Require Import ssreflect ssrfun ssrbool.
From mathcomp Require Import eqtype ssrnat div prime. 

Fixpoint fibonacci (x: nat) := match x with
	| 0 => 1
	| (S x') => match x' with
		| 0 => 1
		| (S x'') => (fibonacci x') + (fibonacci x'')
		end
	end.

Compute fibonacci 22.

