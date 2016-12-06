openerp.folder_management = function(instance, local) {
    instance.kanban-box = instance.web.form.AbstractField.extend({
        template: "kanban-box",
        init: function (view, code) {
            this._super(view, code);
        },
        // The key part:
        render_value: function() { debugger;
            this.$el[0].src = this.get("value");
        }
    });
    instance.web.form.widgets.add('kanban-box', 'instance.kanban-box');
}