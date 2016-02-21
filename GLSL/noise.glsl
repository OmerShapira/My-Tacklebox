// Weyl Integer-Based Hash Generator
// https://www.shadertoy.com/view/MsV3z3

float hash(in ivec2 c)
{
  int x = c.x;
  int y = c.y;
  x = 0x3504f333*x*x+y;
  y = 0xf1bbcdcb*y*y+c.x;
  int r = x*y;
    
    
  return float(r)*(2.0/8589934592.0)+0.5;
}
