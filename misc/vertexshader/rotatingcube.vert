in vec2 texcoord;
in vec4 vPosition;
in vec4 vColor;

out vec4 color;
out vec2 st;

uniform vec3 theta;

void main()
{ 
  mat4 rx, ry, rz;
  vec3 c = cos(theta);
  vec3 s = sin(theta);
  rz = mat4(c.z, -s.z, 0.0, 0.0,
            s.z, c.z, 0.0, 0.0,
            0.0, 0.0, 1.0, 0.0,
            0.0, 0.0, 0.0, 1.0);
  ry = mat4(c.y, 0.0, s.y, 0.0,
            0.0, 1.0, 0.0, 0.0,
            -s.y, 0.0, c.y, 0.0,
            0.0, 0.0, 0.0, 1.0);
  rx = mat4(1.0, 0.0, 0.0, 0.0,
            0.0, c.x, -s.x, 0.0,
            0.0, s.x, c.x, 0.0,
            0.0, 0.0, 0.0, 1.0);
  gl_Position = rz*ry*rx*vPosition;
  color = vColor;
  st = texcoord;
}
