#include <iostream>
#include <ccs/ccs.h>

int main() {
  ccs::CcsDomain ccs;
  std::istringstream input("baz.bar : frob = 'nitz'");
  ccs.loadCcsStream(input, "<literal>", ccs::ImportResolver::None);
  ccs::CcsContext ctx = ccs.build().constrain("baz", {"bar"});
  if (ctx.getString("frob") != "nitz") return 1;
  return 0;
}
