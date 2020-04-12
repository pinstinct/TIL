# tmux

## About tmux

tmux는 터미널에서 실행되는 프로그램이다. tmux 안에서 여러 개의 다른 터미널 프로그램을 실행할 수 있으며, tmux 안의 각 터미널은 tmux가 관리하는 자체 터미널이다. 이것을 멀티플렉싱(multiplexing)이라고 부르며, tmux는 터미널 멀티플렉서(multiplexer)이다.

tmux는 실행 중인 외부 터미널(the outside terminal)에서 분리(detached)될 수 있고, 나중에 동일한 터미널에 다시 연결(reattached)될 수 있다.

tmux의 주요 용도는 다음과 같다.
- 원격 서버에서 실행 중인 프로그램을 tmux 내에서 실행하여 연결이 끊기는 것을 보호
- 여러 다른 로컬 컴퓨터에서 원격 서버에 실행 중인 프로그램에 접근
- 하나의 터미널에서 여러 프로그램과 셸을 함께 사용(like window manager)

## Basic concepts


