# hw3后端部分

本项目使用的后端环境和 hw2 完全相同，所以不在重复构建镜像，使用的是 [hw2-backend](https://github.com/ds-hw-fuuzen/hw2-backend) 的镜像。

[![Docker](https://github.com/ds-hw-fuuzen/hw2-backend/actions/workflows/docker-publish.yml/badge.svg)](https://github.com/ds-hw-fuuzen/hw2-backend/actions/workflows/docker-publish.yml)

[使用 VSCode + docker 开发](https://github.com/ds-hw-fuuzen/.github/blob/main/profile/README.md)

为了实现前后端对接，请在 VSCode 创建开发容器之前先创建这样一个 docker bridge：

```shell shell
docker network create hw3_bridge
```

这个网桥 `hw3_bridge` 名称已经硬编码在 `.devcontainer/docker-compose.yml` 中。

当需要对接的时候，请打开两个 VSCode 窗口，分别在开发容器中打开项目目录，分别运行程序即可。