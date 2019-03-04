subroutine main(n,r)
 implicit none
 integer, intent(in):: n
 integer, intent(out):: r
 call fac(n,r)
end
subroutine fac(n,r)
 integer :: i
 integer, intent(in):: n
 integer, intent(out):: r
  r = 1
  do i=1,n
    r = r*i
  end do
end subroutine