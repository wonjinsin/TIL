## vim관련 설정

만약 e,b같은걸 눌렀을떄 키가 쭉 안움직일때 설정

```
defaults write -g ApplePressAndHoldEnabled -bool false
defaults write -g InitialKeyRepeat -int 10
defaults write -g KeyRepeat -int 1
```
