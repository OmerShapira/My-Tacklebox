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



//Valve Screen Space Dither
// https://www.youtube.com/watch?v=JO7G38_pxU4 at 55:45
//HLSL
float3 ScreenSpaceDither(float2 vScreenPos)
{
	//lestyn's RGB dither (7 asm instructions) from Portal 2 X360, slightly modified for VR
	float3 vDither = dot (float2(171.0, 231.0), vScreenPos.xy + g_flTime).xxx;
	vDither.rgb = frac(vDither.rgb) / float3(103.0, 71.0, 97.0)) - float3(0.5, 0.5, 0.5);
	return (vDither.rgb / 255.0) * 0.375;
}