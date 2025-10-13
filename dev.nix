{
  pkgs ? import <nixpkgs> {}
}:
pkgs.mkShell {
  buildInputs = with pkgs; [
    nodejs_20
    python311
    doas
    cron
    rsync
    vim
  ];
}
