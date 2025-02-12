<!--
  - Tencent is pleased to support the open source community by making BK-ITSM 蓝鲸流程服务 available.
  - Copyright (C) 2021 THL A29 Limited, a Tencent company.  All rights reserved.
  - BK-ITSM 蓝鲸流程服务 is licensed under the MIT License.
  -
  - License for BK-ITSM 蓝鲸流程服务:
  - -------------------------------------------------------------------
  -
  - Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
  - documentation files (the "Software"), to deal in the Software without restriction, including without limitation
  - the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
  - and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
  - The above copyright notice and this permission notice shall be included in all copies or substantial
  - portions of the Software.
  -
  - THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT
  - LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN
  - NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
  - WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
  - SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE
  -->

<template>
    <div class="bk-sops-node-content">
        <div class="bk-page bk-auto-node-basic">
            <p class="bk-header-bold">{{ $t('m.newCommon["基本信息"]') }}</p>
            <div class="bk-main bk-flex">
                <div class="bk-node-name">
                    <span>{{ $t('m.newCommon["节点名称"]') }} : </span>
                    <span>{{nodeInfo.name || '--'}}</span>
                </div>
            </div>
        </div>
        <div class="bk-page bk-auto-node-basic">
            <p class="bk-header-bold">{{ $t('m.newCommon["任务参数"]') }}</p>
            <div>
                <div class="bk-param">
                    <get-param
                        ref="getParam"
                        :is-static="true"
                        :is-static-data="nodeInfo.api_info.sops_info">
                    </get-param>
                </div>
            </div>
        </div>
        <div class="bk-page bk-auto-node-basic">
            <p class="bk-header-bold">{{ $t('m.taskTemplate["执行详情"]') }}</p>
            <div>
                <p class="bk-partition">
                    <b class="bk-base-label">{{ $t('m.taskTemplate["执行状态："]') }}</b>
                    <span
                        :class="{
                            'statusShow': true,
                            'statusSuccess': status === '执行成功',
                            'statusRunning': status === '执行中',
                            'statusFailed': status === '执行失败' }">
                        {{status || '--'}}</span>
                </p>
                <p class="bk-partition">
                    <b class="bk-base-label">{{ $t('m.taskTemplate["任务详情："]') }}</b>
                    <template v-if="nodeInfo.api_info.sops_task_url">
                        <a :href="nodeInfo.api_info.sops_task_url"
                            target="_blank"
                            style="color: #5482F4;">
                            {{ $t('m.taskTemplate["跳转标准运维查看"]') }}
                        </a>
                    </template>
                    <template v-else>
                        <span style="color: #DC5D5D;">{{ $t('m.taskTemplate["任务创建失败"]') }}</span>
                    </template>
                </p>
                <p class="bk-partition">
                    <b class="bk-base-label">{{ $t('m.common["开始时间："]') }}</b>
                    <span>{{nodeInfo.create_at}}</span>
                </p>
                <p class="bk-partition">
                    <b class="bk-base-label">{{ $t('m.common["结束时间："]') }}</b>
                    <span>{{ nodeInfo.end_at || $t('m.taskTemplate["尚未结束"]') }}
                    </span>
                </p>
                <div class="bk-partition errorDiv">
                    <b class="bk-base-label">{{ $t('m.taskTemplate["错误信息："]') }}</b>
                </div>
                <div class="langError">{{nodeInfo.api_info.error_message || '--'}}</div>
            </div>
        </div>
    </div>
</template>

<script>
    import getParam from '@/views/processManagement/processDesign/nodeConfigue/components/sopsGetParam.vue'

    export default {
        name: 'sopsNodeInfo',
        components: {
            getParam
        },
        props: {
            nodeInfo: {
                type: Object,
                default () {
                    return {}
                }
            },
            // 自动节点信息
            apiInfo: {
                type: Object,
                default () {
                    return {}
                }
            }
        },
        data () {
            return {
                status: '',
                errorLength: ''
            }
        },
        mounted () {
            this.status = this.nodeInfo.api_info.sops_result
            this.errorLength = this.nodeInfo.api_info.error_message ? this.nodeInfo.api_info.error_message.length : 0
        }
    }
</script>

<style scoped lang='scss'>
    @import '../../../../scss/mixins/clearfix.scss';
    @import '../../../../scss/mixins/scroller.scss';
    
    .bk-sops-node-content {
        font-size: 14px;
        color: #63656E;

        .bk-header-bold {
            font-weight: bold;
            padding: 10px 0;
        }
    }

    .bk-page {
        display: block;
        height: auto;
        margin-bottom: 10px;

        .bk-flex {
            display: flex;
            // align-items: center;
            flex-wrap: wrap;

            & > div {
                width: 50%;
                line-height: 2;
            }
        }

        .errorDiv {
            display: inline-block;
            position: relative;
            top: -285px;
        }

        .bk-partition {
            padding: 10px 0;
            font-size: 12px;
            .statusShow {
                border-radius: 2px;
                color: white;
                font-size: 10px;
                margin-left: 14px;
            }

            .statusSuccess {
                background: #4EBB49;
            }

            .statusRunning {
                background: #4C7CF4;
            }

            .statusFailed {
                background: #DC5D5D;
            }

            & > span, a {
                margin: 10px;
                padding: 1px 4px;
            }
        }

        .langError {
            @include scroller;
            display: inline-block;
            padding: 2px 4px;
            margin-top: 10px;
            margin-left: 10px;
            height: 300px;
            width: 80%;
            overflow-y: auto;
            overflow-x: hidden;
            word-wrap: break-word;
            word-break: break-all;
        }
    }
    .bk-base-label {
        font-weight: bold;
    }
    .bk-node-name {
        width: 100%;
        font-size: 12px;
    }
</style>
